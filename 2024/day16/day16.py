import heapq
# 작은값이 제일앞에 있음;;


f = open("2024/day16/day16.txt", 'r')

data = []
while True:
    line = f.readline()
    if not line: break

    spl = line.split('\n')[0]
    data.append(list(spl))
    
f.close()



def find_lowest_score(maze):
    rows, cols = len(maze), len(maze[0])
    start = None
    end = None

    # 시작(S)과 종료(E) 찾기
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)

    # 방향: 동쪽, 북쪽, 서쪽, 남쪽
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    pq = [(0, start[0], start[1], 0)]  # (점수, x, y, 방향)
    visited = set()
    
    while pq:
        score, x, y, direction = heapq.heappop(pq)

        # 종료점에 도달하면 점수 반환
        if (x, y) == end:
            print(score, x, y, direction)
            print(pq)

            return score

        # 이미 방문한 위치는 무시
        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        # 앞으로 이동
        nx, ny = x + directions[direction][0], y + directions[direction][1]
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
            heapq.heappush(pq, (score + 1, nx, ny, direction))

        # 좌회전
        left_direction = (direction + 1) % 4
        heapq.heappush(pq, (score + 1000, x, y, left_direction))

        # 우회전
        right_direction = (direction - 1) % 4
        heapq.heappush(pq, (score + 1000, x, y, right_direction))
    return -1


# 함수 호출
lowest_score = find_lowest_score(data)
print(lowest_score)
