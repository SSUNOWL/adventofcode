from collections import deque
track = []
D = open("2024/day20/day20.txt").read().strip()
for line in D.split('\n'):
    spl = line.split('\n')[0]
    track.append(list(spl))


def find_shortest_path(track):
    rows = len(track)
    cols = len(track[0])
    
    # 시작점과 끝점 찾기
    start = None
    end = None
    for r in range(rows):
        for c in range(cols):
            if track[r][c] == 'S':
                start = (r, c)
            elif track[r][c] == 'E':
                end = (r, c)

    # BFS 초기화
    queue = deque([(start, 0)])  # (현재 위치, 거리)
    visited = set()
    visited.add(start)
    parent = {start: None}  # 부모 노드 추적

    # 이동 방향 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        (current_r, current_c), distance = queue.popleft()

        # 도착지점에 도달했을 때
        if (current_r, current_c) == end:
            # 경로 추적
            path = []
            while (current_r, current_c) is not None and parent[(current_r, current_c)] is not None:
                path.append((current_r, current_c))
                current_r, current_c = parent[(current_r, current_c)]
            path.reverse()  # 경로를 역순으로 반환
            return distance, path  # 거리와 경로 반환

        # 다음 위치 탐색
        for dr, dc in directions:
            new_r, new_c = current_r + dr, current_c + dc
            if 0 <= new_r < rows and 0 <= new_c < cols:
                if track[new_r][new_c] in ('.', 'E', '1', '2') and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    parent[(new_r, new_c)] = (current_r, current_c)  # 부모 노드 설정
                    queue.append(((new_r, new_c), distance + 1))

    return -1, []  # 도착지점에 도달할 수 없는 경우


shot = find_shortest_path(track)

rows = len(track)
cols = len(track[0])
res = []
for r in range(rows):
    for c in range(cols):
        if track[r][c] == '#':
            st_p = (r, c)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for (dx, dy) in directions:
                if 0 <= (r + dx) < rows and 0 <= (c + dy) < cols:
                    changed_map = [arr[:] for arr in track]
                    
                    changed_map[r][c] = '1'
                    if changed_map[r + dx][c +dy] == '#':
                        changed_map[r +dx][c + dy] = '2'
                    print(r, c)
                    res.append([(r, c), (r + dx, c +dy),find_shortest_path(changed_map)])


res1 = 0

print(shot[0])
for i in res:
    if shot[0] - i[2][0] >= 100:
        flag = True
        if track[i[1][0]][i[1][1]] !='#':
            if i[0] not in i[2][1] or i[1] not in i[2][1]:
                flag = False
            else:
                if i[2][1].index(i[0]) > i[2][1].index(i[1]):
                    flag = False
        else:
            flag = False
            
        if flag:
            res1 += 1
print(res1)