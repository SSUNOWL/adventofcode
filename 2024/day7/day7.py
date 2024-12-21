

f = open("day7.txt", 'r')

data = []
while True:
    line = f.readline()
    if not line: break
    spl = []
    spl.append(line.split(':')[0])
    for i in line.split(': ')[1].split(' '):
        spl.append(i)
    data.append(spl)

    

f.close()


def conn(x, y):
    return int(str(x) + str(y))

def dus(a, y, now):
    duss = []

    if ( now < len(y)):
        for i in a:
            duss.append(int(i) + int(y[now]))
            duss.append(int(i) * int(y[now]))
            duss.append(conn(int(i), int(y[now]))) #part2
        return dus(duss, y, now + 1)
    else:
        return a

result = 0
flag = False
for qes in data:
    now = 2

    for res in dus([qes[1]], qes, now):
        if int(qes[0]) == int(res):
            flag = True
    if flag:
        result += int(qes[0])
        flag = False
    
print(result)