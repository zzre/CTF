from pwn import *
sys.setrecursionlimit(10**9)

with open("./weather", "rb") as f:
    e = f.read()

ipt = [ord('T')] + [0]*0x2000

S = list(e[0x4080:0x5080])
S += ipt

D = [0]*32

def parse(s: str, debug=False):
    result = []
    s = s.split('%')[1:]

    for _format in s:
        res = ''
        v6 = ''
        v7 = ''
        width = ''
        prec = ''
        sign = ''
        spec = _format[-1]
        _format = _format[:-1]
        v7d = v6d = False

        if _format[0] == '-':
            sign = '-'
            v7 = 'S[{}]'
            _format = _format[1:]
        elif _format[0] == '+':
            sign = '+'
            v7 = 'S[D[{}]]'
            v7d = True
            _format = _format[1:]
        else:
            sign = _format[0]
            v7 = 'D[{}]'
            v7d = True

        if spec == 'C':
            if '.' in _format:
                width, prec = map(int, _format.split('.'))
            else:
                width, prec = int(_format), 0
            
            res = f'C S[{width}] {prec*4} {sign}'
            result.append(res)
            continue
        elif spec == 'M':
            op = '='
        elif spec == 'S':
            op = '+='
        elif spec == 'O':
            op = '-='
        elif spec == 'X':
            op = '*='
        elif spec == 'V':
            op = '//='
        elif spec == 'N':
            op = '%='
        elif spec == 'L':
            op = '<<='
        elif spec == 'R':
            op = '>>='
        elif spec == 'E':
            op = '^='
        elif spec == 'I':
            op = '&='
        elif spec == 'U':
            op = '|='

        if 'hh' in _format:
            v6 = 'S[{}]'
            _format = _format[:-2]
        elif 'h' in _format:
            v6 = 'S[D[{}]]'
            v6d = True
            _format = _format[:-1]
        elif 'll' in _format:
            v6 = '{}'
            _format = _format[:-2]
        elif 'l' in _format:
            v6 = 'D[{}]'
            v6d = True
            _format = _format[:-1]
        else:
            print(f"[!] format error : {_format}")
            exit()
        
        width, prec = map(int, _format.split("."))

        if v7d: width *= 4
        if v6d: prec *= 4

        res = ' '.join([v7.format(width), op, v6.format(prec)])
        result.append(res)

    if debug:
        print('\n'.join(result))
    return result

# C S[width] prec sign(pad)
def execute(x, op, y=None, sign=None):
    global S, D
    if x == 'C':
        check = False
        idx = int(y)
        d = int.from_bytes(bytes(D[idx:idx+4]), 'little')
        if sign == '-':
            check = d >= 0x80000000
        elif sign == '+':
            check = d < 0x80000000
        else:
            check = sign != '0' or d == 0

        if check:
            idx = int(op[2:-1])
            _s = bytes(S[idx:]).split(b'\x00')[0].decode()
            if _s == "%4.5000llM%0.13200llM%337C%0.0llM%500C%1262C%0653.0C":
                debug()
                dump()
                exit()
            res = parse(_s, False)
            for _s in res:
                execute(*_s.split())

        return
    xx = yy = 0
    x_idx = y_idx = 0
    if '[' in x[2:-1]:
        x_idx = int(x[2:-1][2:-1])
        x_idx = eval(f"{x[2:-1][:2]}x_idx:x_idx+4]")
        x_idx = int.from_bytes(bytes(x_idx), 'little')
    else:
        x_idx = eval(f"{x[2:-1]}")
    
    if op == "=":
        if '[' in y:
            if '[' in y[2:-1]:
                y_idx = int(y[2:-1][2:-1])
                y_idx = eval(f"{y[2:-1][:2]}y_idx:y_idx+4]")
                y_idx = int.from_bytes(bytes(y_idx), 'little')
                exec(f"{x[:2]}x_idx:x_idx+4] = {y[:2]}y_idx:y_idx+4]")
            else:
                y_idx = eval(f"{y[2:-1]}")
                exec(f"{x[:2]}x_idx:x_idx+4] = {y[:2]}y_idx:y_idx+4]")
        else:
            exec(f"{x[:2]}x_idx:x_idx+4] = list(int.to_bytes(int(y), 4, 'little'))")
    
    else:
        xx = eval(f"{x[:2]}x_idx:x_idx+4]")

        xx = int.from_bytes(bytes(xx), 'little')

        if '[' in y:
            y_idx = eval(f"{y[2:-1]}")
            yy = eval(f"{y[:2]}y_idx:y_idx+4]")        
            yy = int.from_bytes(bytes(yy), 'little')
        else:
            yy = int(y)

        xx = eval(f"xx {op[:-1]} yy")
        xx &= 0xffffffff
        xx = list(int.to_bytes(xx, 4, 'little'))

        exec(f"{x[:2]}x_idx:x_idx+4] = xx")


def debug():
    _s = bytes(S[52:])
    idx = 52
    while _s:
        try:
            start = _s.index(b'%')
            end = start + _s[start:].index(b'\x00')
            print(f'==== S[{idx+start}] ====')
            print(_s[start:end].decode())
            parse(_s[start:end].decode(), True)
            print()
        
            idx += end
            _s = _s[end:]

        except:
            break

def dump():
    with open("s.dump", "wb") as f:
        f.write(bytes(S))

formats = parse(bytes(S[52:]).split(b'\x00')[0].decode(), False)
for z in formats:
    execute(*z.split())
    