import sys
sys.setrecursionlimit(10**7)
import copy

f = open("2024/day6/day6_input.txt", 'r')

data = []
while True:
    line = f.readline()
    if not line: break
    spl = list(line.split('\n')[0])
    data.append(spl)
    

f.close()

seen = set()
block = set()
row = len(data[0])
height = len(data)
p2 = 0
al_seen = set()


def move(pos, dir):
    seen.add(pos)
    pos2 = pos
    dir2 = dir
    pos += dir
    tmp = copy.deepcopy(data)
    (x, y) = (int(pos.real), int(pos.imag))
    if 0 <= x < row and 0 <= y < height:
        if tmp[y][x] != '#':
            tmp[y][x] = 'O'
            O = True
        else:
            O = False
    else:
        O = False
    if O and pos not in block:
        seen2 = set()
        flag = True
        num = 0
        while (pos2, dir2) not in seen2 and (pos2, dir2) not in al_seen:
            num += 1
            seen2.add((pos2, dir2))
            pos2 += dir2
            (x2, y2) = (int(pos2.real), int(pos2.imag))
            if 0 <= x2 < row and 0 <= y2 < height:
                if tmp[y2][x2] == '#' or tmp[y2][x2] == 'O':
                    pos2 -= dir2

                    dir2 *= 1j
                    
                
            else:
                flag = False
                break
        if flag:
            global p2
            p2 += 1
            block.add(pos)
        print(num)
    al_seen.add((pos2, dir2))
  



    if 0 <= x < row and 0 <= y < height:
        
        if data[y][x] == '#':
            pos -= dir

            dir *= 1j
        move(pos, dir)
    else:
        return 0
    

def solve(part2):
    for y in range(height):
        for x in range(row):
            if data[y][x] == '^':
                pos = x + y * 1j
                dir = 0 -1j
                move(pos, dir)
                print(len(seen))
                print(len(block))
                print(p2)
                print(block)

solve(True)

