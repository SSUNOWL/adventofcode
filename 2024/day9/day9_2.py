import sys
sys.setrecursionlimit(10**7)

f = open("day9.txt", 'r')

while True:
    line = f.readline()
    if not line: break
    data = line.split('\n')[0]
    

    

f.close()


file = []

num = 0
for i in range(0, len(data)):
    if i % 2 == 0:
        file.append([int(data[i]), num])
        num += 1
    else:
        if int(data[i]) > 0:
            file.append([int(data[i]), '.'])




def change(file, N):
    flag = False
    for i in range(len(file) - 1, -1, -1):
        if file[i][1] == N:
            for j in range(0, i):
                if file[j][1] == '.':
                    if file[j][0] >= file[i][0]:
                        flag = True
                        num = i
                        dot = j
                        count = file[i][0]
                        break
                if flag:
                    break


    if flag:
        [c, n] = file[num][0], file[num][1]
        file[dot][0] -= count
        file[num][1] = '.'
        file.insert(dot, [c, n])

    if N > 0:
        N -= 1
        return change(file, N)
    else:
        return file

change(file, num)




result = 0
num = 0
for i in file:
    for j in range(0, i[0]):
        if i[1] != '.':
            result += i[1] * num
        num += 1


print(result)
