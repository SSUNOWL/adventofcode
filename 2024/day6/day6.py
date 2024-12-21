import sys
sys.setrecursionlimit(10**7)

f = open("day6_input.txt", 'r')

data = []
while True:
    line = f.readline()
    if not line: break
    spl = line.split('\n')[0]
    data.append(spl)
    

f.close()

seen = set()
seen2 = set()
block = set()
row = len(data[0])
height = len(data)



def move(pos, dir, part2):
    
    seen.add(pos)

    seen2.clear()
    global data
    tmp = data.copy()
    pos2 = pos
    dir2 = dir
    pos2 += dir
    (x, y) = (int(pos2.real), int(pos2.imag))
    if 0 <= x < row and 0 <= y < height:
        toO = list(data[y])
        toO[x] = 'O'
        data[y] = ''.join(toO)
    flag = True
    while (pos2, dir2) not in seen2:
        pos2 -= dir2
        seen2.add((pos2, dir2))
        print(seen2)
        pos2 += dir2
        (x, y) = (int(pos2.real), int(pos2.imag))

        if 0 <= x < row and 0 <= y < height:
            if data[y][x] == '#' or data[y][x] == 'O':
                pos2 -= dir2

                dir *= 1j
            else:
                pos2 += dir2
            seen2.add((pos2, dir2))
        else:
            flag = False
            break
    if flag:
        block.add(pos2)
        
        
        
    data = tmp.copy()
    pos += dir
    

    (x, y) = (int(pos.real), int(pos.imag))
    if 0 <= x < row and 0 <= y < height:
        
        if data[y][x] == '#':
            pos -= dir

            dir *= 1j
        move(pos, dir, part2)
    else:
        return 0
    

def solve(part2):
    for y in range(height):
        for x in range(row):
            if data[y][x] == '^':
                pos = x + y * 1j
                dir = 0 -1j
                move(pos, dir, part2)
                print(len(seen))
                print(len(block))

solve(True)

