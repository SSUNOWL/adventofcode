from functools import cache

f = open("2024/day17/day17.txt", 'r')

data = {}
while True:
    line = f.readline()
    if not line: break

    spl = line.split('\n')[0]
    if spl != '':
        if spl.count('Register') > 0:
            data[spl.split(' ')[1].split(':')[0]] = int(spl.split(' ')[2])
        else:
            data[spl.split(' ')[0].split(':')[0]] = spl.split(' ')[1].replace(',', '')

f.close()
@cache
def combo(A, B, C, opr):
    a = int(opr)
    if a > 3:
        if a == 4:
            return A
        elif a == 5:
            return B
        elif a == 6:
            return C
        elif a == 7:
            return
    else:
        return a

def opcode(A, B, C, code, opr, pos):
    code = int(code)
    opr = int(opr)
    comb_opr = combo(A, B, C, opr)
    pos += 2
    if code == 0:
        A = int(A / (2 ** comb_opr))
    elif code == 1:
            B = B ^ opr
    elif code == 2:
        B = comb_opr % 8
    elif code == 3:
        if A != 0:
            pos = opr
    elif code == 4:
        B = int(B ^ C)
    elif code == 5:
        res1.append(comb_opr % 8)
    elif code == 6:
        B = int(A / (2 ** comb_opr))
    elif code == 7:
        C = int(A / (2 ** comb_opr))
    



    return A, B, C, pos


length = len(data['Program'])
pos = 0

A = data['A']

B = data['B']
C = data['C']
code = data['Program'][pos]
opr = data['Program'][pos + 1]
res1 = []


copy = []
for i in data['Program']:
    copy.append(int(i))
print(copy)
num =  1


while num < 99999999:
    pos = 0
    A = num
    res1.clear()

    while pos < length:


        (A, B, C, pos) = opcode(A, B, C, code, opr, pos)
        if pos >= length:
            break
        code = data['Program'][pos]
        opr = data['Program'][pos + 1]


    print(num, res1)
    num += 1
