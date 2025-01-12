f = open("2024/day25/day25.txt", 'r')

lock = []
key = []
data = []

while True:
    line = f.readline()
    if not line: break
    spl = line.split('\n')[0]

    if spl == '':
        if data[0][0] == '.':
            key.append(data)
        elif data[0][0] == '#':
            lock.append(data)
        data = []
    else:
        data.append(list(spl))

    
f.close()

row = len(key[0][0])
height = len(key[0])
key_hi = []
lock_hi = []

for s in key:
    pin = {}
    for j in range(height):
        for i in range(row):
            if s[j][i] == '#':
                if i in pin.keys():
                    if pin[i] > j:
                        pin[i] == j
                else:
                    pin[i] = j

    hi = []
    for pi in sorted(pin.keys()):
        hi.append(6 - pin[pi])
    key_hi.append(hi)

    pin.clear()
    

for s in lock:
    pin = {}
    for j in range(height - 1, -1, -1):
        for i in range(row):
            if s[j][i] == '#':
                if i in pin.keys():
                    if pin[i] < j:
                        pin[i] == j
                else:
                    pin[i] = j

    hi = []
    for pi in sorted(pin.keys()):
        hi.append(pin[pi])
    lock_hi.append(hi)

    pin.clear()
    
flag = True
res = 0
for l in lock_hi:
    for k in key_hi:
        for i in range(row):
            if l[i] + k[i] >= 6:
                flag = False
        if flag:
            res += 1
        else:
            flag = True
print(res)