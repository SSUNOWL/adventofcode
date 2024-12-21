from collections import deque

# 방향 정의: 동, 북, 서, 남
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def is_valid(x, y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#'

def bfs(maze, start, end):
    queue = deque()
    visited = set()
    best_paths = set()  # 최적 경로에 포함된 타일을 저장할 집합
    min_score = float('inf')

    # (x, y, 방향, 점수, 타일 개수)
    queue.append((start[0], start[1], 0, 0, 1))
    visited.add((start[0], start[1], 0))

    while queue:
        x, y, direction, score, tile_count = queue.popleft()

        # 종료 조건
        if (x, y) == end:
            if score < min_score:
                min_score = score
                best_paths.clear()  # 새로운 최적 경로가 발견되면 이전 경로 삭제
            if score == min_score:
                best_paths.add((x, y))  # 현재 타일 추가
            continue

        # 전진
        dx, dy = directions[direction]
        if is_valid(x + dx, y + dy, maze):
            if (x + dx, y + dy, direction) not in visited:
                visited.add((x + dx, y + dy, direction))
                queue.append((x + dx, y + dy, direction, score + 1, tile_count + 1))
                best_paths.add((x + dx, y + dy))  # 타일 추가

        # 회전
        for turn in [-1, 1]:  # 왼쪽 회전, 오른쪽 회전
            new_direction = (direction + turn) % 4
            if (x, y, new_direction) not in visited:
                visited.add((x, y, new_direction))
                queue.append((x, y, new_direction, score + 1000, tile_count))

    return best_paths

# 미로 입력
maze = [
    "###############",
    "#.......#....E#",
    "#.#.###.#.###.#",
    "#.....#.#...#.#",
    "#.###.#####.#.#",
    "#.#.#.......#.#",
    "#.#.#####.###.#",
    "#...........#.#",
    "###.#.#####.#.#",
    "#...#.....#.#.#",
    "#.#.#.###.#.#.#",
    "#.....#...#.#.#",
    "#.###.#.#.#.#.#",
    "#S..#.....#...#",
    "###############"
]

# 시작과 종료 좌표
start = (13, 1)  # S의 위치
end = (1, 11)    # E의 위치

# BFS 실행
best_path_tiles = bfs(maze, start, end)
print("최적 경로에 포함된 타일의 개수:", len(best_path_tiles))
