
from z3 import *
import subprocess

s = Solver()
x = [BitVec(f'x{i}', 8) for i in range(58)]

s.add(And(
    x[0] == ord('f'),
    x[1] == ord('l'),
    x[2] == ord('a'),
    x[3] == ord('g'),
    x[4] == ord('{'),
    x[57] == ord('}')
))

for i in range(5, 57):
    s.add(
        Or(
            And(ord('a') <= x[i], x[i] <= ord('z')),
            And(ord('0') <= x[i], x[i] <= ord('9')),
            #And(ord('A') <= x[i], x[i] <= ord('Z')),
            x[i] == ord('_')
        )
    )

akimotoite = x[50]
covellite=x[9]
halloysite = x[24]
s.add(akimotoite * 8 * (covellite - 4) * (halloysite + 4) == 9711352)
chalcocite = x[54]
allanite=x[13]
akimotoite = x[35]
s.add(chalcocite * 7 * (allanite - 3) * (akimotoite + 3) == 3764768)
akimotoite = x[57]
kurnakovite=x[45]
chalcocite = x[19]
s.add(akimotoite * 2 * (kurnakovite - 8) * (chalcocite + 1) == 1248000)
fayalite = x[41]
covellite=x[35]
chalcocite = x[11]
s.add(fayalite * 7 * (covellite - 2) * (chalcocite + 5) == 7452648)
fayalite = x[25]
covellite=x[27]
akimotoite = x[3]
s.add(fayalite * 1 * (covellite - 7) * (akimotoite + 7) == 1013650)
allanite = x[54]
covellite=x[41]
akimotoite = x[31]
s.add(allanite * 9 * (covellite - 5) * (akimotoite + 6) == 4860261)
covellite = x[12]
kurnakovite=x[24]
pyrophanite = x[50]
s.add(covellite * 3 * (kurnakovite - 6) * (pyrophanite + 4) == 3261825)
pyrophanite = x[23]
aerinite=x[19]
covellite = x[8]
s.add(pyrophanite * 7 * (aerinite - 4) * (covellite + 9) == 8149680)
aerinite = x[39]
chalcocite=x[50]
clinohumite = x[56]
s.add(aerinite * 7 * (chalcocite - 4) * (clinohumite + 1) == 7864857)
pyrophanite = x[45]
halloysite=x[56]
akimotoite = x[57]
s.add(pyrophanite * 5 * (halloysite - 8) * (akimotoite + 5) == 3276000)
allanite = x[7]
pyrophanite=x[47]
akimotoite = x[23]
s.add(allanite * 9 * (pyrophanite - 9) * (akimotoite + 1) == 4164210)
halloysite = x[20]
clinohumite=x[43]
pyrophanite = x[5]
s.add(halloysite * 7 * (clinohumite - 2) * (pyrophanite + 5) == 8704850)
clinohumite = x[45]
kurnakovite=x[52]
covellite = x[45]
s.add(clinohumite * 6 * (kurnakovite - 1) * (covellite + 8) == 1032192)
aerinite = x[46]
allanite=x[45]
kurnakovite = x[44]
s.add(aerinite * 8 * (allanite - 9) * (kurnakovite + 4) == 3647952)
pyrophanite = x[29]
kurnakovite=x[32]
covellite = x[44]
s.add(pyrophanite * 5 * (kurnakovite - 7) * (covellite + 1) == 5339520)
covellite = x[53]
akimotoite=x[33]
kurnakovite = x[9]
s.add(covellite * 6 * (akimotoite - 4) * (kurnakovite + 1) == 6170472)
kurnakovite = x[15]
allanite=x[42]
covellite = x[4]
s.add(kurnakovite * 1 * (allanite - 1) * (covellite + 7) == 1502280)
chalcocite = x[12]
covellite=x[54]
aerinite = x[1]
s.add(chalcocite * 7 * (covellite - 3) * (aerinite + 2) == 3364900)
akimotoite = x[19]
kurnakovite=x[24]
clinohumite = x[45]
s.add(akimotoite * 9 * (kurnakovite - 3) * (clinohumite + 9) == 6748560)
clinohumite = x[32]
akimotoite=x[43]
allanite = x[8]
s.add(clinohumite * 9 * (akimotoite - 9) * (allanite + 7) == 12196800)
halloysite = x[28]
fayalite=x[35]
akimotoite = x[47]
s.add(halloysite * 6 * (fayalite - 7) * (akimotoite + 7) == 3124176)
pyrophanite = x[25]
fayalite=x[3]
covellite = x[18]
s.add(pyrophanite * 6 * (fayalite - 7) * (covellite + 2) == 6128640)
akimotoite = x[11]
allanite=x[30]
chalcocite = x[0]
s.add(akimotoite * 2 * (allanite - 4) * (chalcocite + 6) == 2268864)
clinohumite = x[16]
pyrophanite=x[21]
fayalite = x[25]
s.add(clinohumite * 4 * (pyrophanite - 6) * (fayalite + 5) == 5192000)
chalcocite = x[9]
halloysite=x[39]
fayalite = x[46]
s.add(chalcocite * 9 * (halloysite - 6) * (fayalite + 8) == 11118870)
pyrophanite = x[37]
allanite=x[46]
kurnakovite = x[6]
s.add(pyrophanite * 8 * (allanite - 4) * (kurnakovite + 2) == 8096784)
kurnakovite = x[50]
halloysite=x[45]
aerinite = x[19]
s.add(kurnakovite * 3 * (halloysite - 9) * (aerinite + 6) == 1552269)
akimotoite = x[52]
pyrophanite=x[22]
clinohumite = x[31]
s.add(akimotoite * 7 * (pyrophanite - 6) * (clinohumite + 3) == 3495856)
aerinite = x[53]
chalcocite=x[32]
kurnakovite = x[30]
s.add(aerinite * 8 * (chalcocite - 3) * (kurnakovite + 7) == 9647120)
pyrophanite = x[28]
akimotoite=x[40]
covellite = x[32]
s.add(pyrophanite * 6 * (akimotoite - 7) * (covellite + 3) == 5918940)
pyrophanite = x[24]
covellite=x[57]
fayalite = x[50]
s.add(pyrophanite * 5 * (covellite - 4) * (fayalite + 3) == 7235800)
fayalite = x[40]
allanite=x[25]
akimotoite = x[17]
s.add(fayalite * 3 * (allanite - 3) * (akimotoite + 8) == 3025236)
covellite = x[26]
pyrophanite=x[37]
fayalite = x[51]
s.add(covellite * 9 * (pyrophanite - 6) * (fayalite + 2) == 4297293)
clinohumite = x[29]
chalcocite=x[25]
halloysite = x[4]
s.add(clinohumite * 2 * (chalcocite - 1) * (halloysite + 7) == 2639520)
aerinite = x[1]
halloysite=x[8]
pyrophanite = x[20]
s.add(aerinite * 7 * (halloysite - 1) * (pyrophanite + 1) == 7402752)
covellite = x[49]
pyrophanite=x[38]
halloysite = x[35]
s.add(covellite * 6 * (pyrophanite - 5) * (halloysite + 2) == 3299940)
akimotoite = x[16]
chalcocite=x[34]
covellite = x[19]
s.add(akimotoite * 1 * (chalcocite - 2) * (covellite + 2) == 1226610)
covellite = x[50]
fayalite=x[10]
halloysite = x[44]
s.add(covellite * 2 * (fayalite - 2) * (halloysite + 6) == 2203416)
akimotoite = x[56]
kurnakovite=x[15]
clinohumite = x[40]
s.add(akimotoite * 7 * (kurnakovite - 2) * (clinohumite + 1) == 7126168)
kurnakovite = x[36]
halloysite=x[47]
chalcocite = x[57]
s.add(kurnakovite * 5 * (halloysite - 2) * (chalcocite + 9) == 3797560)
halloysite = x[39]
kurnakovite=x[24]
chalcocite = x[42]
s.add(halloysite * 2 * (kurnakovite - 7) * (chalcocite + 8) == 2931552)
clinohumite = x[23]
halloysite=x[24]
allanite = x[0]
s.add(clinohumite * 6 * (halloysite - 6) * (allanite + 3) == 7210350)
halloysite = x[16]
chalcocite=x[39]
clinohumite = x[39]
s.add(halloysite * 6 * (chalcocite - 5) * (clinohumite + 3) == 9515520)
akimotoite = x[0]
kurnakovite=x[13]
halloysite = x[53]
s.add(akimotoite * 4 * (kurnakovite - 5) * (halloysite + 6) == 4667520)
kurnakovite = x[37]
akimotoite=x[15]
halloysite = x[24]
s.add(kurnakovite * 4 * (akimotoite - 3) * (halloysite + 2) == 4766580)
kurnakovite = x[0]
fayalite=x[42]
clinohumite = x[32]
s.add(kurnakovite * 4 * (fayalite - 4) * (clinohumite + 2) == 4752384)
pyrophanite = x[32]
akimotoite=x[21]
aerinite = x[12]
s.add(pyrophanite * 7 * (akimotoite - 6) * (aerinite + 8) == 8724100)
aerinite = x[21]
kurnakovite=x[6]
chalcocite = x[26]
s.add(aerinite * 6 * (kurnakovite - 3) * (chalcocite + 4) == 7598928)
pyrophanite = x[41]
chalcocite=x[18]
halloysite = x[30]
s.add(pyrophanite * 9 * (chalcocite - 7) * (halloysite + 7) == 11513340)
halloysite = x[25]
clinohumite=x[43]
kurnakovite = x[13]
s.add(halloysite * 2 * (clinohumite - 4) * (kurnakovite + 9) == 2756520)
kurnakovite = x[13]
clinohumite=x[26]
aerinite = x[55]
s.add(kurnakovite * 3 * (clinohumite - 2) * (aerinite + 5) == 3480360)
aerinite = x[1]
chalcocite=x[20]
pyrophanite = x[55]
s.add(aerinite * 9 * (chalcocite - 7) * (pyrophanite + 8) == 9152352)
pyrophanite = x[53]
kurnakovite=x[26]
fayalite = x[35]
s.add(pyrophanite * 6 * (kurnakovite - 2) * (fayalite + 5) == 5703600)
aerinite = x[51]
pyrophanite=x[27]
kurnakovite = x[37]
s.add(aerinite * 8 * (pyrophanite - 6) * (kurnakovite + 9) == 4238304)
kurnakovite = x[53]
clinohumite=x[0]
akimotoite = x[42]
s.add(kurnakovite * 7 * (clinohumite - 7) * (akimotoite + 5) == 7364210)
allanite = x[32]
aerinite=x[5]
pyrophanite = x[56]
s.add(allanite * 8 * (aerinite - 4) * (pyrophanite + 7) == 9332400)
allanite = x[54]
clinohumite=x[2]
covellite = x[32]
s.add(allanite * 1 * (clinohumite - 5) * (covellite + 4) == 513912)
clinohumite = x[24]
fayalite=x[6]
aerinite = x[13]
s.add(clinohumite * 3 * (fayalite - 7) * (aerinite + 4) == 4187610)
kurnakovite = x[23]
pyrophanite=x[46]
aerinite = x[36]
s.add(kurnakovite * 6 * (pyrophanite - 6) * (aerinite + 7) == 6723360)
pyrophanite = x[36]
aerinite=x[14]
kurnakovite = x[32]
s.add(pyrophanite * 5 * (aerinite - 8) * (kurnakovite + 2) == 6287120)
akimotoite = x[31]
fayalite=x[9]
halloysite = x[42]
s.add(akimotoite * 5 * (fayalite - 3) * (halloysite + 5) == 5820630)
aerinite = x[47]
covellite=x[54]
clinohumite = x[16]
s.add(aerinite * 1 * (covellite - 8) * (clinohumite + 3) == 267894)
allanite = x[34]
clinohumite=x[56]
pyrophanite = x[43]
s.add(allanite * 5 * (clinohumite - 7) * (pyrophanite + 5) == 5790330)
chalcocite = x[30]
clinohumite=x[49]
covellite = x[16]
s.add(chalcocite * 6 * (clinohumite - 6) * (covellite + 6) == 3856896)
allanite = x[40]
pyrophanite=x[0]
akimotoite = x[22]
s.add(allanite * 9 * (pyrophanite - 6) * (akimotoite + 3) == 8967456)
covellite = x[52]
kurnakovite=x[57]
fayalite = x[14]
s.add(covellite * 6 * (kurnakovite - 3) * (fayalite + 3) == 4088952)
clinohumite = x[57]
allanite=x[28]
covellite = x[37]
s.add(clinohumite * 2 * (allanite - 4) * (covellite + 6) == 2394750)
akimotoite = x[15]
allanite=x[51]
pyrophanite = x[3]
s.add(akimotoite * 9 * (allanite - 2) * (pyrophanite + 2) == 5000940)
pyrophanite = x[27]
covellite=x[11]
chalcocite = x[17]
s.add(pyrophanite * 2 * (covellite - 8) * (chalcocite + 5) == 2127840)
allanite = x[36]
clinohumite=x[28]
halloysite = x[56]
s.add(allanite * 7 * (clinohumite - 6) * (halloysite + 7) == 7290465)
halloysite = x[57]
kurnakovite=x[9]
allanite = x[30]
s.add(halloysite * 1 * (kurnakovite - 5) * (allanite + 1) == 1362500)
covellite = x[5]
fayalite=x[28]
aerinite = x[50]
s.add(covellite * 7 * (fayalite - 9) * (aerinite + 9) == 7114800)
covellite = x[27]
clinohumite=x[24]
akimotoite = x[29]
s.add(covellite * 8 * (clinohumite - 9) * (akimotoite + 7) == 10142080)
chalcocite = x[11]
pyrophanite=x[21]
covellite = x[36]
s.add(chalcocite * 1 * (pyrophanite - 8) * (covellite + 4) == 1232604)
kurnakovite = x[30]
allanite=x[48]
aerinite = x[5]
s.add(kurnakovite * 5 * (allanite - 8) * (aerinite + 9) == 2585520)
kurnakovite = x[36]
akimotoite=x[11]
clinohumite = x[9]
s.add(kurnakovite * 6 * (akimotoite - 4) * (clinohumite + 7) == 7105056)
fayalite = x[0]
kurnakovite=x[14]
covellite = x[11]
s.add(fayalite * 3 * (kurnakovite - 1) * (covellite + 4) == 3534300)
aerinite = x[16]
halloysite=x[9]
covellite = x[22]
s.add(aerinite * 8 * (halloysite - 4) * (covellite + 7) == 10583184)
chalcocite = x[49]
pyrophanite=x[28]
kurnakovite = x[19]
s.add(chalcocite * 5 * (pyrophanite - 6) * (kurnakovite + 9) == 2751840)
halloysite = x[46]
pyrophanite=x[27]
akimotoite = x[16]
s.add(halloysite * 1 * (pyrophanite - 1) * (akimotoite + 2) == 1211280)
halloysite = x[1]
allanite=x[34]
chalcocite = x[43]
s.add(halloysite * 3 * (allanite - 6) * (chalcocite + 2) == 3785940)
akimotoite = x[27]
allanite=x[45]
aerinite = x[56]
s.add(akimotoite * 5 * (allanite - 5) * (aerinite + 7) == 2784600)
kurnakovite = x[53]
chalcocite=x[52]
fayalite = x[8]
s.add(kurnakovite * 4 * (chalcocite - 3) * (fayalite + 7) == 1983520)
halloysite = x[8]
akimotoite=x[45]
chalcocite = x[5]
s.add(halloysite * 8 * (akimotoite - 7) * (chalcocite + 7) == 4522112)
chalcocite = x[44]
fayalite=x[8]
clinohumite = x[44]
s.add(chalcocite * 6 * (fayalite - 4) * (clinohumite + 9) == 5868720)
chalcocite = x[56]
clinohumite=x[1]
fayalite = x[6]
s.add(chalcocite * 1 * (clinohumite - 9) * (fayalite + 3) == 1086624)
aerinite = x[6]
halloysite=x[2]
akimotoite = x[16]
s.add(aerinite * 7 * (halloysite - 8) * (akimotoite + 7) == 8488375)
pyrophanite = x[16]
aerinite=x[42]
fayalite = x[41]
s.add(pyrophanite * 8 * (aerinite - 4) * (fayalite + 8) == 11388416)
fayalite = x[29]
clinohumite=x[50]
covellite = x[11]
s.add(fayalite * 1 * (clinohumite - 6) * (covellite + 8) == 1118340)
fayalite = x[3]
covellite=x[43]
kurnakovite = x[2]
s.add(fayalite * 8 * (covellite - 1) * (kurnakovite + 2) == 9789120)
pyrophanite = x[0]
covellite=x[25]
clinohumite = x[54]
s.add(pyrophanite * 3 * (covellite - 3) * (clinohumite + 2) == 1435752)
chalcocite = x[12]
allanite=x[34]
pyrophanite = x[48]
s.add(chalcocite * 3 * (allanite - 8) * (pyrophanite + 6) == 1484280)
allanite = x[24]
aerinite=x[19]
kurnakovite = x[7]
s.add(allanite * 4 * (aerinite - 5) * (kurnakovite + 7) == 4688320)
allanite = x[48]
covellite=x[15]
clinohumite = x[52]
s.add(allanite * 2 * (covellite - 8) * (clinohumite + 1) == 500000)
akimotoite = x[35]
chalcocite=x[30]
pyrophanite = x[4]
s.add(akimotoite * 9 * (chalcocite - 4) * (pyrophanite + 7) == 11559600)
fayalite = x[41]
covellite=x[44]
aerinite = x[14]
s.add(fayalite * 9 * (covellite - 6) * (aerinite + 5) == 10034928)
fayalite = x[32]
halloysite=x[7]
kurnakovite = x[53]
s.add(fayalite * 2 * (halloysite - 7) * (kurnakovite + 5) == 2039400)
fayalite = x[55]
aerinite=x[43]
pyrophanite = x[19]
s.add(fayalite * 9 * (aerinite - 9) * (pyrophanite + 3) == 10577952)
pyrophanite = x[56]
fayalite=x[48]
aerinite = x[10]
s.add(pyrophanite * 4 * (fayalite - 5) * (aerinite + 9) == 2099160)
pyrophanite = x[12]
covellite=x[32]
akimotoite = x[18]
s.add(pyrophanite * 8 * (covellite - 3) * (akimotoite + 4) == 9270480)

while True:
    if s.check() != sat:
        break

    m = s.model()
    res = [int(m[i].as_long()) for i in x]
    flag = ''.join(map(chr, [res[i] for i in range(58)]))

    print(f"[-] try : {flag}")

    p = subprocess.Popen(["python3.9", "eunectes-murinus.pyc"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stderr, stdout = p.communicate(flag.encode())

    if b"Success" in stderr:
        print()
        print(f"[*] flag : {flag}")
        break
