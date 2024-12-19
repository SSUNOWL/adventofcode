f = open("day15.txt", 'r')

data = []
togo = ""
while True:
    line = f.readline()
    if not line: break

    spl = line.split('\n')[0]
    if spl.count('#') > 0:
        spl = list(spl)

        all_shop_index = list(filter(lambda x: list(spl)[x] == '#', range(len(list(spl)))))

        for a in reversed(all_shop_index):
            spl.insert(a, '#')
        all_dot_index = list(filter(lambda x: list(spl)[x] == '.'  or list(spl)[x] == '@', range(len(list(spl)))))

        for a in reversed(all_dot_index):
            spl.insert(a + 1, '.')
        all_O_index = list(filter(lambda x: list(spl)[x] == 'O', range(len(list(spl)))))

        for o in reversed(all_O_index):
            spl[o] = ']'
            spl.insert(o, '[')
        

        
        data.append(spl)
    else:
        togo += spl


f.close()


def move(pos, dir):
    rob_pos = pos
    pos += dir
    (x, y) = (int(pos.real), int(pos.imag))
    stack = 0
    moving = False
    boxes = set()

    if data[y][x] == '[' or ']':
        if data[y][x+1] == ']':
            boxes.add(((x, y), (x + 1, y)))
        if data[y][x-1] =='[':
            boxes.add(((x, y), (x + 1, y)))
    for box in boxes:
        left = box[0][0] + box[0][1] * 1j
        right = box[1][0] + box[1][1] * 1j
        left += dir
        right += dir
        (lex, ley) = (int(left.real), int(left.imag))
        (rix, riy) = (int(right.real), int(right.imag))

        if data[ley][lex] == '#' or data[riy][rix] == '#':
            #끝 not move 하나만 #이어도 됨됨
            print(boxes)
        elif data[ley][lex] == '.' or data[riy][rix] == '.':
            #끝 move 모든 상자의 dir방향이 .이어야함
            print(boxes)
        elif data[ley][lex] == '[' or data[riy][rix] == '[' or data[ley][lex] == ']' or data[riy][rix] == ']':
            #boxes에 추가
            boxes.add
        



for i in data:
    print(i)