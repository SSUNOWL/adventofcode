f = open("2024/day15/day15.txt", 'r')

data = []
all_boxes = set()
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

# 왼쪾 박스를 좌표의 기준으로 둠
def move_leri(pos, dir):
    (dx, dy) = dir
    (x, y) = pos
    while data[y + dy][x + dx] in ('[', ']'):
        
        if data[y + dy][x + dx] == '[' or data[y + dy][x + dx] == ']':
            dx += dir[0]
        

    if data[y + dy][x + dx] == '.':
        popped = data[y + dy].pop(x + dx)
        data[y].insert(x, popped)
        return (x + dir[0], y + dy)

    elif data[y + dy][x + dx] == '#':
        dx = 0
        return (x , y + dy)


def move_ud(pos, dir):
    boxes = set()
    (dx, dy) = dir
    (x, y) = pos        
    # @가 박스 하나를 찾은 경우
    flag = False
    if data[y + dy][x + dx] == '[':
        boxes.add((x + dx, y + dy))
        flag = True
        
    elif data[y + dy][x + dx] == ']':
        boxes.add((x + dx - 1, y + dy))
        flag = True
    elif data[y + dy][x + dx] == '.':
        flag = True
    # 모든 박스의 진행방향이 . 이거나 ; 한박스의 진행방향에 #이 있는경우 멈춤
    new_box = set()
    while flag:
        new_box.clear()

        for box in boxes:
            (box_x, box_y) = box
            if data[box_y + dy][box_x + dx] == '#' or data[box_y + dy][box_x + dx +1] == '#':
                flag = False
                break
            elif data[box_y + dy][box_x + dx] in ('[', ']', '.') or data[box_y + dy][box_x + dx +1] in ('[', ']', '.'):
                if data[box_y + dy][box_x + dx] == '[':
                    new_box.add((box_x + dx, box_y + dy))
                if data[box_y + dy][box_x + dx] == ']':
                    new_box.add((box_x + dx - 1, box_y + dy))
                if data[box_y + dy][box_x + dx +1] == '[':
                    new_box.add((box_x + dx + 1, box_y + dy))
                if data[box_y + dy][box_x + dx +1] == ']':
                    new_box.add((box_x + dx, box_y + dy))
                
        if len(new_box - boxes) > 0:
            boxes.update(new_box)
            continue
        else:
            break
    if flag:
        if dy > 0:
            boxes = sorted(boxes, key=lambda x: -x[1])
        else:
            boxes = sorted(boxes, key=lambda x: x[1])
        for box in boxes:
            
            (box_x, box_y) = box
            data[box_y][box_x] = '.'
            data[box_y][box_x + 1] = '.'
            data[box_y + dy][box_x] = '['
            data[box_y + dy][box_x + 1] = ']'
        data[y][x] = '.'
        data[y + dy][x] = '@' 
        return (x + dx, y + dy)
    else:
        return (x + dx, y)
            
        




for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '@':
            pos = (x, y)
(x, y) = pos
for tg in togo:
    
    if tg == '<':
        (x, y) = move_leri((x, y), (-1, 0))
    elif tg == '>':
        (x, y) = move_leri((x, y), (1, 0))
    elif tg == '^':
        (x, y) = move_ud((x, y), (0, -1))
    elif tg == 'v':
        (x, y) = move_ud((x, y), (0, 1))
    



res = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '[':
            res += 100 * i + j
print(res)