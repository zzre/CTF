'''
> readRDS("373")
function (flag)
{
    check_val_0() & check_val_1(94, 82, 6) & check_val_2() &
        check_val_1(1, 86, 10) & check_val_3() & check_val_1(90,
        83, 9) & check_val_1(9, 11, 15) & check_val_4() & check_val_1(29,
        61, 57) & check_val_5() & check_val_6(67, 71, 22103) &
        check_val_6(72, 76, 50138) & check_val_7() & check_val_8() &
        check_val_9() & (substr(get_flag_or_die(), 6, 6) == "b") &
        check_val_6(37, 41, 19230) & check_val_6(43, 47, 11202) &
        check_val_10() & check_val_11(76, "8") & check_val_11(93,
        "3") & check_val_11(13, "0") & check_val_6(77, 79, 763) &
        check_val_6(85, 87, 303) & check_val_6(59, 61, 753) &
        check_val_12() & check_val_11(26, "5") & check_val_13() &
        check_val_14() & check_val_11(87, "3") & check_val_15() &
        check_val_11(88, "c") & check_val_16() & check_val_17() &
        check_val_11(81, "0") & check_val_11(86, "0") & check_val_11(17,
        "1") & check_val_11(18, "a") & check_val_6(39, 41, 230) &
        check_val_6(21, 23, 361) & check_val_11(39, "2") & check_val_11(58,
        "2") & check_val_6(51, 53, 713) & check_val_6(33, 35,
        351) & check_val_11(19, "2") & check_val_11(20, "b") &
        check_val_11(31, "3") & check_val_6(45, 47, 202) & check_val_11(44,
        "1") & check_val_11(49, "3") & check_val_11(55, "3") &
        check_val_11(44, "1") & check_val_11(45, "2") & check_val_6(63,
        65, 707) & check_val_11(66, "c")
}
<bytecode: 0x563c0e16af50>
> readRDS("122E")
function ()
{
    flag <- get_flag_or_die()
    val_1 <- substr(flag, 14, 14)
    val_2 <- substr(flag, 18, 18)
    val_3 <- substr(flag, 24, 24)
    val_4 <- substr(flag, 32, 32)
    val_5 <- substr(flag, 36, 36)
    val_6 <- substr(flag, 62, 62)
    (val_1 == val_2) & (val_1 == "a") & (val_1 == val_3) & (val_3 ==
        val_4) & (val_5 == val_4) & (val_6 == val_5)
}
<bytecode: 0x563c0e186608>
> readRDS("1561")
function (index, val)
{
    flag <- get_flag_or_die()
    val_1 <- substr(flag, index, index)
    val_1 == val
}
<bytecode: 0x563c0e19ec50>
> readRDS("16DA")
function ()
{
    flag <- get_flag_or_die()
    val_1 <- substr(flag, 72, 72)
    val_2 <- substr(flag, 92, 92)
    val_3 <- substr(flag, 26, 26)
    val_4 <- substr(flag, 34, 34)
    val_5 <- substr(flag, 60, 60)
    (val_1 == val_2) & (val_1 == val_3) & (val_1 == val_4) &
        (val_1 == val_5)
}
<bytecode: 0x563c0e1b5fa8>
> readRDS("198D")
function ()
{
    flag <- get_flag_or_die()
    val_1 <- substr(flag, 22, 22)
    val_2 <- substr(flag, 48, 48)
    val_3 <- substr(flag, 78, 78)
    val_4 <- substr(flag, 89, 89)
    (val_1 == val_2) & (val_1 == val_3) & (val_1 == val_4)
}
<bytecode: 0x563c0e1cc4f0>
> readRDS("1BF5")
function ()
{
    flag <- get_flag_or_die()
    val_1 <- substr(flag, 51, 51)
    val_2 <- substr(flag, 59, 59)
    val_3 <- substr(flag, 63, 63)
    val_4 <- substr(flag, 65, 65)
    val_5 <- substr(flag, 77, 77)
    val_6 <- substr(flag, 91, 91)
    (val_1 == val_2) & (val_1 == val_3) & (val_1 == val_4) &
        (val_1 == val_5) & (val_1 == val_6)
}
<bytecode: 0x563c0e1deff8>
> readRDS("1EFA")
function ()
{
    flag <- get_flag_or_die()
    val_1 <- as.integer(substr(flag, 51, 51))
    val_2 <- as.integer(substr(flag, 22, 22))
    (val_1 - val_2) == 1
}
<bytecode: 0x563c0e1f7070>
> readRDS("20F9")
function ()
{
    flag <- get_flag_or_die()
    val_1 <- substr(flag, 17, 17)
    val_2 <- substr(flag, 23, 23)
    val_3 <- substr(flag, 28, 28)
    val_4 <- substr(flag, 35, 35)
    val_5 <- substr(flag, 37, 37)
    val_6 <- substr(flag, 43, 43)
    val_7 <- substr(flag, 44, 44)
    val_8 <- substr(flag, 52, 52)
    val_9 <- substr(flag, 69, 69)
    val_10 <- substr(flag, 74, 74)
    (val_1 == val_2) & (val_1 == val_3) & (val_1 == val_4) &
        (val_1 == val_5) & (val_1 == val_6) & (val_1 == val_7) &
        (val_1 == val_8) & (val_1 == val_9) & (val_1 == val_10)
}
<bytecode: 0x563c0e20c0f0>
> readRDS("2535")
function ()
{
    flag <- get_flag_or_die()
    val_1 <- as.integer(substr(flag, 17, 17))
    val_2 <- as.integer(substr(flag, 87, 87))
    (val_1 - val_2) == -2
}
<bytecode: 0x563c0e2210c8>
> readRDS("273F")
function ()
{
    flag <- get_flag_or_die()
    val_1 <- as.integer(substr(flag, 7, 8))
    val_2 <- as.integer(substr(flag, 9, 10))
    val_3 <- as.integer(substr(flag, 89, 91))
    val_4 <- as.integer(substr(flag, 92, 93))
    ((val_1 - val_2) == 9) & ((val_3 + val_4) == 680)
}
<bytecode: 0x563c0e239f08>
> readRDS("2A27")
function ()
{
    flag <- get_flag_or_die()
    x <- 9
    delayedAssign("y", x)
    x <- x * (x - 5 + 4 + 6 - 3 - 2 - 3 - 6)
    as.integer(substr(flag, 1, 1)) == y
}
<bytecode: 0x563c0e24c7e0>
> readRDS("2CC1")
function ()
{
    flag <- get_flag_or_die()
    as.integer(substr(flag, 25, 29)) == 25213
}
<bytecode: 0x563c0e267308>
> readRDS("2E40")
function ()
{
    flag <- get_flag_or_die()
    as.integer(substr(flag, 7, 11)) == 29202
}
<bytecode: 0x563c0e27a900>
> readRDS("2FBE")
function (index_0, index_1, val)
{
    flag <- get_flag_or_die()
    as.integer(substr(flag, index_0, index_1)) == val
}
<bytecode: 0x563c0e28dd70>
> readRDS("3148")
function ()
{
    flag <- get_flag_or_die()
    val_1 <- substr(flag, 16, 16)
    val_2 <- substr(flag, 30, 30)
    (val_1 == val_2) & (val_1 == "f")
}
<bytecode: 0x563c0e2a1288>
> readRDS("332A")
function ()
{
    flag <- get_flag_or_die()
    val_1 <- substr(flag, 42, 42)
    val_2 <- substr(flag, 50, 50)
    val_3 <- substr(flag, 56, 56)
    val_4 <- substr(flag, 80, 80)
    (val_1 == val_2) & (val_1 == "d") & (val_1 == val_3) & (val_3 ==
        val_4)
}
<bytecode: 0x563c0e2b4340>
> readRDS("35BD")
function ()
{
    flag <- get_flag_or_die()
    val_1 <- substr(flag, 54, 54)
    val_2 <- substr(flag, 84, 84)
    val_3 <- substr(flag, 12, 12)
    (val_1 == val_2) & (val_1 == "e") & (val_1 == val_3)
}
<bytecode: 0x563c0e2ce8f8>
> readRDS("37F5")
function ()
{
    if (exists("flag", envir = .GlobalEnv)) {
        flag_value <- get("flag", envir = .GlobalEnv)
        if (is.character(flag_value)) {
            xor_key <- "BHMEAISTHEBESTCTFEVERBETTERTHANALLOFTHEOTHERCTF"
            key_length <- nchar(xor_key)
            flag_length <- nchar(flag_value)
            if (flag_length != key_length) {
                xor_key <- substr(rep(xor_key, length.out = ceiling(flag_length/key_length)),
                  1, flag_length)
            }
            xor_result <- sapply(1:flag_length, function(i) {
                flag_char <- substr(flag_value, i, i)
                key_char <- substr(xor_key, i, i)
                int_val <- as.integer(charToRaw(flag_char))
                xor_val <- as.integer(charToRaw(key_char))
                xored_val <- bitwXor(int_val, xor_val)
                as.raw(xored_val)
            })
            return(paste0(xor_result, collapse = ""))
        }
    }
    else {
        system("echo 'try better next time'")
    }
}
<bytecode: 0x563c0e2e1630>
'''

from z3 import *

s = Solver()

xor_key = "BHMEAISTHEBESTCTFEVERBETTERTHANALLOFTHEOTHERCTF"
flag = [BitVec(f'flag{i}', 64) for i in range(100)]

val_1 = flag[14]
val_2 = flag[18]
val_3 = flag[24]
val_4 = flag[32]
val_5 = flag[36]
val_6 = flag[62]
s.add(val_1 == val_2)
s.add(val_1 == ord('a'))
s.add(val_1 == val_3)
s.add(val_3 == val_4)
s.add(val_5 == val_4)
s.add(val_6 == val_5)

s.add(flag[76] == ord('8'))
s.add(flag[93] == ord('3'))
s.add(flag[13] == ord('0'))
s.add(flag[26] == ord('5'))
s.add(flag[87] == ord('3'))
s.add(flag[88] == ord('c'))
s.add(flag[81] == ord('0'))
s.add(flag[86] == ord('0'))
s.add(flag[17] == ord('1'))
s.add(flag[18] == ord('a'))
s.add(flag[39] == ord('2'))
s.add(flag[58] == ord('2'))
s.add(flag[19] == ord('2'))
s.add(flag[20] == ord('b'))
s.add(flag[31] == ord('3'))
s.add(flag[44] == ord('1'))
s.add(flag[49] == ord('3'))
s.add(flag[55] == ord('3'))
s.add(flag[44] == ord('1'))
s.add(flag[45] == ord('2'))
s.add(flag[66] == ord('c'))

val_1 = flag[72]
val_2 = flag[92]
val_3 = flag[26]
val_4 = flag[34]
val_5 = flag[60]
s.add(val_1 == val_2)
s.add(val_1 == val_3)
s.add(val_1 == val_4)
s.add(val_1 == val_5)

val_1 = flag[22]
val_2 = flag[48]
val_3 = flag[78]
val_4 = flag[89]
s.add(val_1 == val_2)
s.add(val_1 == val_3)
s.add(val_1 == val_4)

val_1 = flag[51]
val_2 = flag[59]
val_3 = flag[63]
val_4 = flag[65]
val_5 = flag[77]
val_6 = flag[91]
s.add(val_1 == val_2)
s.add(val_1 == val_3)
s.add(val_1 == val_4)
s.add(val_1 == val_5)
s.add(val_1 == val_6)

# val_1 = flag[51]
# val_2 = flag[22]
# s.add(val_1 - val_2 == 1)

val_1 = flag[17]
val_2 = flag[23]
val_3 = flag[28]
val_4 = flag[35]
val_5 = flag[37]
val_6 = flag[43]
val_7 = flag[44]
val_8 = flag[52]
val_9 = flag[69]
val_10 = flag[74]
s.add(val_1 == val_2)
s.add(val_1 == val_3)
s.add(val_1 == val_4)
s.add(val_1 == val_5)
s.add(val_1 == val_6)
s.add(val_1 == val_7)
s.add(val_1 == val_8)
s.add(val_1 == val_9)
s.add(val_1 == val_10)

# val_1 = flag[17]
# val_2 = flag[87]
# s.add(val_1 - val_2 == -2)

# val_1 = (flag[7] << 8) + flag[8]
# val_2 = (flag[9] << 8) + flag[10]
# val_3 = (flag[89] << 8) + flag[91]
# val_4 = (flag[92] << 8) + flag[93]
# s.add((val_1 - val_2) == 9)
# s.add((val_3 + val_4) == 680)

x = 9
y = x * (x - 5 + 4 + 6 - 3 - 2 - 3 - 6)
s.add(flag[1] == ord(str(y)))

s.add(flag[25] == ord(str(2)))
s.add(flag[26] == ord(str(5)))
s.add(flag[27] == ord(str(2)))
s.add(flag[28] == ord(str(1)))
s.add(flag[29] == ord(str(3)))

s.add(flag[7] == ord(str(2)))
s.add(flag[8] == ord(str(9)))
s.add(flag[9] == ord(str(2)))
s.add(flag[10] == ord(str(0)))
s.add(flag[11] == ord(str(2)))

val_1 = flag[16]
val_2 = flag[30]
s.add(val_1 == val_2)
s.add(val_1 == ord('f'))

val_1 = flag[42]
val_2 = flag[50]
val_3 = flag[56]
val_4 = flag[80]
s.add(val_1 == val_2)
s.add(val_1 == ord('d'))
s.add(val_1 == val_3)
s.add(val_3 == val_4)

val_1 = flag[54]
val_2 = flag[84]
val_3 = flag[12]
s.add(val_1 == val_2)
s.add(val_1 == ord('e'))
s.add(val_1 == val_3)

s.add(flag[67] == ord(str(2)))
s.add(flag[68] == ord(str(2)))
s.add(flag[69] == ord(str(1)))
s.add(flag[70] == ord(str(0)))
s.add(flag[71] == ord(str(3)))

s.add(flag[72] == ord(str(5)))
s.add(flag[73] == ord(str(0)))
s.add(flag[74] == ord(str(1)))
s.add(flag[75] == ord(str(3)))
s.add(flag[76] == ord(str(8)))

s.add(flag[37] == ord(str(1)))
s.add(flag[38] == ord(str(9)))
s.add(flag[39] == ord(str(2)))
s.add(flag[40] == ord(str(3)))
s.add(flag[41] == ord(str(0)))

s.add(flag[43] == ord(str(1)))
s.add(flag[44] == ord(str(1)))
s.add(flag[45] == ord(str(2)))
s.add(flag[46] == ord(str(0)))
s.add(flag[47] == ord(str(2)))

s.add(flag[77] == ord(str(7)))
s.add(flag[78] == ord(str(6)))
s.add(flag[79] == ord(str(3)))

s.add(flag[85] == ord(str(3)))
s.add(flag[86] == ord(str(0)))
s.add(flag[87] == ord(str(3)))

s.add(flag[59] == ord(str(7)))
s.add(flag[60] == ord(str(5)))
s.add(flag[61] == ord(str(3)))

s.add(flag[39] == ord(str(2)))
s.add(flag[40] == ord(str(3)))
s.add(flag[41] == ord(str(0)))

s.add(flag[21] == ord(str(3)))
s.add(flag[22] == ord(str(6)))
s.add(flag[23] == ord(str(1)))

s.add(flag[51] == ord(str(7)))
s.add(flag[52] == ord(str(1)))
s.add(flag[53] == ord(str(3)))

s.add(flag[33] == ord(str(3)))
s.add(flag[34] == ord(str(5)))
s.add(flag[35] == ord(str(1)))

s.add(flag[45] == ord(str(2)))
s.add(flag[46] == ord(str(0)))
s.add(flag[47] == ord(str(2)))

s.add(flag[63] == ord(str(7)))
s.add(flag[64] == ord(str(0)))
s.add(flag[65] == ord(str(7)))

s.add(flag[1] == flag[2])
s.add(flag[1] == flag[3])
s.add(flag[1] == flag[4])
s.add(flag[1] == flag[5])

s.add(flag[6] == ord('b'))

s.add(flag[94] == flag[6])
s.add(flag[82] == flag[6])

s.add(flag[1] == flag[86])
s.add(flag[1] == flag[10])

s.add(flag[83] == flag[90])
s.add(flag[9] == flag[90])

s.add(flag[11] == flag[9])
s.add(flag[15] == flag[9])

s.add(flag[29] == flag[57])
s.add(flag[61] == flag[57])


assert s.check() == sat

m = s.model()
# for i, x in enumerate(flag):
#     if m[x] != None:
#         print(i, chr(m[x].as_long()))
#     else:
#         print(i, None)

ans = [chr(m[x].as_long()) for x in flag[1:95]]
ans = ''.join(ans)

from pwn import xor

print(xor(bytes.fromhex(ans), xor_key))
