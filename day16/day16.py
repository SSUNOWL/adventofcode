from collections import deque

f = open("day16.txt", 'r')

data = []
while True:
    line = f.readline()
    if not line: break

    spl = line.split('\n')[0]
    data.append(list(spl))
    
f.close()


row = len(data[0])
height = len(data)

paths = []

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            print(path)
            paths.append(path)
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < height and data[ny][nx] != '#':
                if (nx, ny) not in path:
                    queue.append([(nx, ny), path + [(nx, ny)]])
                    visited.add((nx, ny))


for y in range(height):
    for x in range(row):
        if data[y][x] == 'S':
            st = (x, y)
        elif data[y][x] == 'E':
            en = (x, y)

bfs(st, en)
res = []

for path in paths:
    r = len(path) - 1
    num = 1

    dir = (path[0][0] - path[1][0]) +  (path[0][1] - path[1][1]) * 1j
    for i in range(1, len(path) - 1):
        dx = path[i][0] - path[i + 1][0]
        dy = path[i][1] - path[i + 1][1]
        ddir = dx + dy * 1j


        if dir * -1j == ddir or dir * 1j == ddir:
            num += 1
        dir = ddir

    r += num * 1000
    res.append(r)
    print(r)
print(min(res))

