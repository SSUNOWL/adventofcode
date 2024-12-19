
f = open("day12.txt", 'r')

data = []
while True:
    line = f.readline()
    if not line: break
    spl = line.split('\n')[0]
    data.append(spl)

f.close()

row = len(data[0])
height = len(data)
SEEN = set()
SEEN_al = set()
dots = dict()

def move(pos, alpha):
    dir = 1j
    SEEN_al.add(pos)
    SEEN.add(pos)

    whi = {1: 0, 2 : 1, 3 : 1j, 4 : 1 + 1j}
    for i in whi.keys():

        if pos+ whi[i] in dots:
            dots[pos+ whi[i]].add(i)
        else:
            dots[pos+whi[i]] = {i}

    for i in range(0, 4):
        next_pos = pos + dir
        x = int(next_pos.real)
        y = int(next_pos.imag)
        
        if 0 <= x < row and 0 <= y < height:
            if data[y][x] == alpha:
                if next_pos not in SEEN_al:

                    SEEN_al.add(next_pos)
                    SEEN.add(next_pos)
                    move(next_pos, alpha)

                                   
            
        dir *= 1j


def solve(part2):
    res = 0
    
    for y in range(0, height):
        for x in range(0, row):
            pos = x + y * 1j
            if pos not in SEEN:
                SEEN_al.clear()
                peri = 4
                dots.clear()
                move(pos, data[y][x])
                
                
                area = len(SEEN_al)
                if not part2:
                    peri = len(SEEN_al) * 4
                    cop = set()
                    for i in SEEN_al:
                        cop.add(i)
                        for j in SEEN_al:
                            if i != j and j not in cop:
                                if (i-j) * (i-j) == 1 or (i-j) * (i-j) == -1:
                                    peri -= 2
                    res += area * peri
                else:
                    line = 0

                    for i in dots.keys():

                        if len(dots[i]) % 2 != 0:
                            line += 1
                        else:
                            flag = False
                            if len(dots[i]) == 2:
                                if (1 in dots[i] and 4 in dots[i]) or (2 in dots[i] and 3 in dots[i]):
                                    flag = True
                                
                            if flag:
                                line += 2
                            
                    res += area * line

                
    return res


print(solve(True))
