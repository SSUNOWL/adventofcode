
f = open("day14.txt", 'r')

d = []
while True:
    line = f.readline()
    if not line: break
    spl = line.split('\n')[0]
    p = (int(spl.split('=')[1].split(' ')[0].split(',')[0]), int(spl.split('=')[1].split(' ')[0].split(',')[1]))
    v = (int(spl.split('=')[2].split(',')[0]), int(spl.split('=')[2].split(',')[1]))

    d.append({'p' : p, 'v' : v})

f.close()


row = 101
height = 103

row_cent = row // 2
height_cent = height // 2


rob = []
def move(pos, vec, sec):
    x = pos[0] + vec[0] * sec
    y = pos[1] + vec[1] * sec

    while x < 0 or x >= row:
        if x < 0:
            x += row
        else:
            x -= row
    while y < 0 or y >= height:
        if y < 0:
            y += height
        else:
            y -= height

    rob.append((x, y))


def solve(part2):
    
    if not part2:
        for i in d:
            move(i['p'], i['v'], 100)
    
        ans = {'1':0, '2':0, '3':0, '4':0}
        for sev in rob:
            if sev[0] == row_cent or sev[1] == height_cent:
                continue
            else:
                if sev[0] < row_cent:
                    if sev[1] < height_cent:
                        ans['1'] += 1
                    else:
                        ans['4'] += 1
                else:
                    if sev[1] < height_cent:
                        ans['2'] += 1
                    else:
                        ans['3'] += 1
        res = 1
        for i in ans.values():
            res *= i
        return res
    else:
        file = open('day14_tree.txt', 'a')
        sec = 5269
        for i in d:
            move(i['p'], i['v'], 0)
        first = rob.copy()
        while True:
            sec += 1
            rob.clear()

            for i in d:
                move(i['p'], i['v'], sec)
            if first == rob:
                break
            ans = []
            for i in range(0, height):
                rows = '.'
                for j in range(0, row - 1):
                    rows += '.'
                ans.append(rows)
            
            for j in rob:
                toa = list(ans[j[1]])
                toa[j[0]] = 'O'
                ans[j[1]] = ''.join(toa)
                
           
            a = file.write(str(sec) + '\n')
            for i in ans:
                a = file.write(i + '\n')
            a = file.write('------------------------------')

# print(solve(False))
solve(True)