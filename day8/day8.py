f = open("day8.txt", 'r')

data = []
while True:
    line = f.readline()
    if not line: break
    spl = line.split('\n')[0]
    data.append(spl)

    

f.close()



ant = {}
anti_node = set()
anti_node2 = set()
nemo = (len(data[0]), len(data))
for y in range (0, len(data)):
    for x in range (0, len(data[y])):
        if data[y][x] != '.':
            if data[y][x] in ant:
                ant[data[y][x]].append((x, y))
                
            else:
                
                xy =  [(x, y)]
                ant[data[y][x]] = xy


for antenna in ant:
    for j in range(0, len(ant[antenna]) - 1):
        for p in range(j + 1, len(ant[antenna])):
            (x1, y1) = ant[antenna][j]
            (x2, y2) = ant[antenna][p]
            new_anti = set()
            new_anti.add((2 * x2 - x1, 2 * y2 - y1))
            new_anti.add((2 * x1 - x2, 2 * y1 - y2))
            if ( x1 == x2 or y1 == y2):
                print(x1, x2, y1, y2)
            new_anti2 = set()
            new_anti2.add((x1, y1))
            new_anti2.add((x2, y2))
            newx = x2
            newy = y2
            while True:
                
                newx += x1 - x2
                newy += y1 - y2
                if (0 <= newx < nemo[0] and 0 <= newy < nemo[1]):
                    new_anti2.add((newx, newy))
                else:
                    break
            newx = x1
            newy = y1
            while True:
                newx += x2 - x1
                newy += y2 -y1
                if (0 <= newx < nemo[0] and 0 <= newy < nemo[1]):
                    new_anti2.add((newx, newy))
                else:
                    break
            anti_node.update(new_anti)
            # print(new_anti2)    
            anti_node2.update(new_anti2)

result = 0
result2 = 0
for x, y in anti_node:
    if 0 <= x < nemo[0] and 0 <= y < nemo[1]:
        result += 1
print(anti_node2)

for x, y in anti_node2:
    if 0 <= x < nemo[0] and 0 <= y < nemo[1]:
        result2 += 1

print(result, result2)

             