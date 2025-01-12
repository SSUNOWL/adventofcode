import itertools 
#집합에서 가능한 모든 경우의 수를 계산해서 대입 후 계산하려고 했는데 너무 오래걸림



f = open("2024/day24/day24.txt", 'r')


value = {}
qes = []
xs = {}
ys = {}
while True:
    line = f.readline()
    if not line: break

    spl = line.split('\n')[0]
    if spl.find(':') > 0:
        value[spl.split(': ')[0]] = int(spl.split(': ')[1])
        if spl[0] == 'x':
            xs[spl.split(': ')[0]] = int(spl.split(': ')[1])
        elif spl[0] == 'y':
            ys[spl.split(': ')[0]] = int(spl.split(': ')[1])
    else:
        if spl != '':
            qes.append(spl.split(' '))
    
f.close()


def calc(qes):
    zs = {}



    while len(qes) > 0:
        idx = []
        idx.clear()
        for i in range(len(qes)):
            if qes[i][0] in value.keys() and qes[i][2] in value.keys():
                if qes[i][1] == 'OR':
                    value[qes[i][4]] = value[qes[i][0]] | value[qes[i][2]]
                elif qes[i][1] == 'XOR':
                    value[qes[i][4]] = value[qes[i][0]] ^ value[qes[i][2]]
                elif qes[i][1] == 'AND':
                    value[qes[i][4]] = value[qes[i][0]] & value[qes[i][2]]
                idx.append(i)
                if qes[i][4][0] == 'z':
                    zs[qes[i][4]] = value[qes[i][4]]
            
        for d in reversed(idx):
            del qes[d]
    return zs

zs = calc(qes)

resz = ''
resx = ''
resy = ''
for i in reversed(sorted(zs.keys())):
    resz += str(zs[i])
  
for i in reversed(sorted(xs.keys())):
    resx += str(xs[i])
for i in reversed(sorted(ys.keys())):
    resy += str(ys[i])

print(bin(int(resx, 2) + int(resy, 2))[2:])
print(resz)
print(int(resx, 2), int(resy, 2), int(resz, 2))

print(int(resz, 2))