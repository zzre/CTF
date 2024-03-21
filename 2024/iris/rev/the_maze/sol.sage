# run on sage
from itertools import product
from collections import defaultdict

def solve():
    matrices = [
        [[-17969, -16540, 11745, -12783, 3226, 15010, 10940, 3387, -5306, -4100, -21425, 10338, -16904, -355, 13485, -25858], 503155],
        [[24356, 12443, -34624, -20408, 7719, 2169, -12039, -4767, -11817, -10941, 24441, 12396, -17878, -8011, 28295, 19198], 138081],
        [[-14826, 3464, 5822, -13182, 51761, -11669, -19467, 45292, 29097, -6763, -10919, 25324, -11126, 2364, 4412, -9672], 10270],
        [[-10870, 13314, 3852, 6736, 8930, -9852, -1980, -5468, -982, 3891, 1980, 3481, 7174, -9705, -4194, -6127], 35766]
    ]

    ret = '''
    finished = true;

    async function pressKey(key) {
        keydownEvent = new KeyboardEvent('keydown', {
            key: key,
            code: key,
            keyCode: key,
            which: key,
        });

        keyupEvent = new KeyboardEvent('keyup', {
            key: key,
            code: key,
            keyCode: key,
            which: key,
        });

        const targetElement = document;
        targetElement.dispatchEvent(keydownEvent);
        await delay(100);
        targetElement.dispatchEvent(keyupEvent);
    }

    function delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    async function checkFinished() {
        while (!finished) {
            await delay(100);
        }
    }

    async function solve() {
        lst = [solve0, solve1, solve2, solve3]
        for (func of lst) {
            finished = false;
            func();
            await checkFinished();
            finished = true;
            i.g = {x: 31, y: 31}
            await pressKey(39);
            console.log(func.name + " done!");
        }
    }

    '''

    script = """
    function solve{idx}() {{
        path = {path};
        let idx = 0;
        async function go() {{
            if (idx < path.length) {{
                const key = path[idx];
                await pressKey(key);
                idx++;
                go();
            }} else {{
                finished = true;
            }}
        }}

        go();
    }}
    
    """

    for idx, (M, c) in enumerate(matrices):
        path = []
        M = Matrix(4, 4, map(lambda x: x / c, M))
        res = M.inverse().coefficients()

        d = {38: 'up', 40: 'down', 37: 'left', 39: 'right'}
        candi = defaultdict(list)

        for lst in product(d, repeat=3):
            j = 1
            for c in lst:
                j = (j << 2) | (3 & c)
            candi[(j & 63) - 32] += [lst]

        # find path
        for i in range(16):
            path += candi[res[i]][0]

        ret += script.format(idx=idx, path=path)

    ret += 'solve();'

    with open('solve.js', 'w') as f:
        f.write(ret)

solve()
