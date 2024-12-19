
f = open("day9.txt", 'r')

while True:
    line = f.readline()
    if not line: break
    data = line.split('\n')[0]
    

    

f.close()


file = []
allfile = 0

num = 0
for i in range(0, len(data)):
    if i % 2 == 0:
        for j in range(0, int(data[i])):
            file.append(num)
        allfile += int(data[i])
        num += 1
    else:
        for j in range(0, int(data[i])):
            file.append('.')


print(file)
x = len(file) - 1

# print(allfile)
while file.index('.') < allfile:
    fir_dot = file.index('.')
    
    tmp = file[x]
    file[x] = file[fir_dot]
    file[fir_dot] = tmp
    x -= 1
    
result = 0
for i in range(0, allfile):
    result += i * int(file[i])

print(file)
print(result)