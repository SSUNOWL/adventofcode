f = open("day5_input.txt", 'r')

result = 0
result2 = 0
data = {}
while True:
    line = f.readline()
    if not line: break
    sep = line.split(',')
    if ( sep[0] in data):
        tmp = data[sep[0]]
        tmp.append(sep[1][0:-1])
        data[sep[0]] = tmp

    else:
        data[sep[0]] = [sep[1][0:-1]]


f.close()

f = open('day5_q.txt', 'r')

qes =[]
while True:
    line = f.readline()
    if not line: break
    sep = line[0:-1].split(',')
    list = []
    for i in sep:
        list.append(i)
    qes.append(list)

f.close()

for i in qes:
    flag = True
    for j in range(0, len(i) - 1):
        for p in range(j+1, len(i)):
            if (i[j] in data):
                # print(i[j], i[p], data[i[j]].count(i[p]))
                if ( data[i[j]].count(i[p]) == 0):
                    flag = False
            else:
                flag = False
    if flag:
        result = result + int(i[int(len(i)/2)])
    else:
        for j in range(0, len(i) - 1):
            for p in range(j+1, len(i)):
                if (i[j] in data):
                    # print(i[j], i[p], data[i[j]].count(i[p]))
                    if ( data[i[j]].count(i[p]) == 0):

                        tmp = i[j]
                        i[j] = i[p]
                        i[p] = tmp
                else:
                        tmp = i[j]
                        i[j] = i[p]
                        i[p] = tmp
        result2 = result2 + int(i[int(len(i)/2)])
        




print(result, result2)