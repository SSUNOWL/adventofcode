import itertools

f = open("2024/day23/day23.txt", 'r')

conn = {}
while True:
    line = f.readline()
    if not line: break

    spl = line.split('\n')[0]
    coms = spl.split('-')
    if coms[0] in conn.keys():
        conn[coms[0]].add(coms[1])
    else:
        conn[coms[0]] = set()
        conn[coms[0]].add(coms[1])

    if coms[1] in conn.keys():
        conn[coms[1]].add(coms[0])
    else:
        conn[coms[1]] = set()
        conn[coms[1]].add(coms[0])
    

f.close()
print(conn)
# others = []
# res = set()
# for com in conn.keys():
#     if com[0] == 't':
#         others.clear()
#         for ot in conn[com]:
#             others.append([com, ot])
#         for ot in conn[com]:
#             for o in others:
#                 if o[0] in conn[ot] and o[1] in conn[ot]:
#                     res.add(frozenset({o[0], o[1], ot}))
# # 세개가 상호 연결되어있음; -> ta:{tb, tc, td} 라고 하면 tb 혹은 tc 혹은 td에 {ta, tb} ; {ta, tc} ; {ta, td} 가 안에 있음
# print(len(res))
def dfs(node, visited):
    stack = [node]
    group = []
    
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            group.append(current)
            for neighbor in conn[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return group

# 모든 컴퓨터를 탐색하여 상호 연결된 그룹 찾기
visited = set()
connected_groups = []

for computer in conn.keys():
    if computer not in visited:
        group = dfs(computer, visited)
        connected_groups.append(group)

# 결과 출력
print("상호 연결된 컴퓨터 그룹:")
for group in connected_groups:
    print(group)
print(connected_groups)