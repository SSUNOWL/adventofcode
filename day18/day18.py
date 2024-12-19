from collections import deque

# 바이트 위치 입력
byte_positions = [
    
]

f = open("day18.txt", 'r')

data = {}
while True:
    line = f.readline()
    if not line: break

    spl = line.split('\n')[0]
    byte_positions.append((int(spl.split(',')[0]), int(spl.split(',')[1])))
    
f.close()

# 메모리 공간 초기화
grid_size = 71  # 예시에서는 0부터 6까지
grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

# 바이트 떨어뜨리기 시뮬레이션
for x, y in byte_positions[:1024]:  # 첫 12바이트만 시뮬레이션
    grid[y][x] = '#'

# BFS를 사용하여 최단 경로 탐색
def bfs(start, goal):
    queue = deque([start])
    visited = set()
    visited.add(start)
    steps = 0

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if (x, y) == goal:
                return steps
            
            # 상하좌우 탐색
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in visited and grid[ny][nx] == '.':
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        
        steps += 1

    return -1  # 경로가 없는 경우

# 출구 좌표
start = (0, 0)
goal = (70, 70)

# 최단 경로 계산
min_steps = bfs(start, goal)
print("최소 단계 수:", min_steps)

more_box = 1022
while min_steps != -1:
    more_box +=1  

    (x, y) = byte_positions[more_box]
    grid[y][x] = '#'
    min_steps = bfs(start, goal)
    print(min_steps, (x, y), more_box)

print(byte_positions[more_box])