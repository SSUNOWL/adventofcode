f = open("day15.txt", 'r')

data = []
togo = ""
while True:
    line = f.readline()
    if not line: break

    spl = line.split('\n')[0]

    if spl.count('#') > 0:
        data.append(list(spl))
    else:
        togo += spl


f.close()


row = len(data[0])
height = len(data)






def move(pos, dir):
    rob_pos = pos
    pos += dir
    (x, y) = (int(pos.real), int(pos.imag))
    stack = 0
    moving = False

    while data[y][x] != '#':
        moving = False

        if data[y][x] == 'O':
            stack += 1
        elif data[y][x] == '.':
            moving = True
            break
        pos += dir
        (x, y) = (int(pos.real), int(pos.imag))

    if moving:

        (x, y) = (int(pos.real), int(pos.imag))

        data[y][x] = 'O'
        pos -= stack * dir
        (x, y) = (int(pos.real), int(pos.imag))
        ret = pos
        data[y][x] = '@'
        pos = rob_pos
        (x, y) = (int(pos.real), int(pos.imag))
        data[y][x] = '.'
        return ret
    return rob_pos



def solve(part2):
    for y in range(height):
        for x in range(row):
            if data[y][x] == '@':
                pos = x + y * 1j
    
    for dir in togo:
        if dir == '^':
            pos = move(pos, -1j)
        elif dir == '>':
            pos = move(pos, 1)
        elif dir == '<':
            pos = move(pos, -1)
        elif dir == 'v':
            pos = move(pos, 1j)

    res = 0
    for y in range(height):
        for x in range(row):
            if data[y][x] == 'O':
                res += x + 100 * y
    return res


                            


        
print(solve(False))


