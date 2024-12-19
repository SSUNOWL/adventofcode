
f = open("day10.txt", 'r')

data = []
while True:
    line = f.readline()
    if not line: break
    spl = line.split('\n')[0]
    data.append(spl)

f.close()

height = len(data)
row  = len(data[0])
p1 = 0
p2 = 0
sum = set()
all = 0
# print(data)

def move(pos, hei):
    if hei == 9:
        global all
        all += 1
        sum.add(pos)
    dir = 1j
    for i in range(0, 4):
        next_pos = pos + dir
        x = int(next_pos.real)
        y = int(next_pos.imag)
        if 0 <= x < row and 0 <= y < height:

            if int(data[y][x]) == hei + 1:

                move(next_pos, hei + 1)
                
            

        dir *= 1j
        

def solve(part2):
    res = 0
    for y in range(0, height):
        for x in range(0, row):
            if data[y][x] == '0':
                pos = x + y * 1j
                sum.clear()
                move(pos, 0)
                if part2:
                    res = all
                else:
                    res += len(sum)
    return res

# p1 = solve(False)
p2 = solve(True)
# print(p1)
print(p2)
# print(all)