import itertools
# 방향을 입력하면 어디에있는지 출력해줌;
# 무엇을 눌러야 되는지에 대한 답은 현재 위치 - 가야 할 위치로 알수 있긴함함 
# 몇번을 눌러야 하는지가 답임
D = open("2024/day21/day21.txt").read().strip()
data = []
for line in D.split('\n'):
    spl = line.split('\n')[0]
    data.append(spl)


qes = '029A'
# -1 2 9 0
start = [[2, 0], [2, 1]]

numpad = [
    ['X', '1', '4', '7'],
    ['0', '2', '5', '8'],
    ['A', '3', '6', '9']
]

keypad = [
    ['<', 'X'],
    ['v', '^'],
    ['>','A']
]

seen = dict()


def push(qes, pos, pad):
    res = []
    result = []

    (x, y) = pos
    for q in qes:
        apart = []
        for xq in range(len(pad)):
            if q in pad[xq]:
                yq = pad[xq].index(q)
                break
        if pad[x][y] + q in seen.keys():
            apart = seen[pad[x][y] + q]
        else:
            dx = xq - x
            dy = yq - y
            flag = [True, True]
            if dx != 0 and dy != 0:
                if pad[x + dx][y] == 'X':
                    flag[0] = False
                if pad[x][y + dy] == 'X':
                    flag[1] = False
            elif dx == 0 and dy == 0:
                flag = [False, False]
            else:
                flag = [True, False]
            if flag[0]:
                res1 = ''
                if dx < 0:
                    res1 += '<' * -dx
                elif dx > 0:
                    res1 += '>' * dx
                if dy < 0:
                    res1 += 'v' * -dy
                elif dy > 0:
                    res1 += '^' * dy
                res1 += 'A'
                apart.append(res1)
            if flag[1]:
                res1 = ''
                if dy < 0:
                    res1 += 'v' * -dy
                elif dy > 0:
                    res1 += '^' * dy
                if dx < 0:
                    res1 += '<' * -dx
                elif dx > 0:
                    res1 += '>' * dx
                res1 += 'A'
                apart.append(res1)
            if not flag[0] and not flag[1]:
                res1 = 'A'
                apart.append(res1)

            if (pad[x][y]+q) not in seen.keys():
                
                seen[pad[x][y] + q] = apart

        res.append(apart)  

        
        
        (x, y) = [xq, yq]
    for i in list(itertools.product(*res, repeat=1)):
        r = ''
        for j in i:
            r += j
        
        result.append(r)
    result = sorted(result, key=len)[:5]
    return result

res1 = 0
for d in data:
    r = list(push(d, start[0], numpad))
    for i in range(2):
        r1 = []
        for k in r:
            r1.append(push(k, start[1], keypad))
        print(i, r1)

        
        r = sorted(list(itertools.chain.from_iterable(r1)))[:5]
    print(min(r))

    res1 += int(d[:3]) * len(min(r))

    
print(res1)
# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
# A가 최초지점

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

# <vA<AA>>^AvAA<^A>Av<<A>>^AvA^A<vA>^Av<<A>^A>AAvA^Av<<A>A>^AAAvA<^A>A
# v<<A>>^AAAvA^A<vA<AA>>^AvAA<^A>Av<<A>A>^AAAvA<^A>A<vA>^A<A>A
# v<<A>>^A<vA<A>>^AAvAA<^A>Av<<A>>^AAvA^A<vA>^AA<A>Av<<A>A>^AAAvA<^A>A
# v<<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>Av<<A>A>^AAvA<^A>A
# v<<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>Av<<A>A>^AAAvA<^A>A

# 029A: <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
# 980A: <v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A
# 179A: <v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
# 456A: <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A
# 379A: <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
