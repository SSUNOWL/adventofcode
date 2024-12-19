f = open("day4.txt", 'r')

data = []
while True:
    line = f.readline()
    if not line: break
    data.append(line[0:-1])
    

f.close()
result = 0
result2 = 0
num = 0

for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if data[y][x] == 'X':
            list = []
            if x + 3 < len(data[y]):
                list.append(data[y][x] + data[y][x+1] + data[y][x+2] + data[y][x+3])
            if x - 3 >= 0:
                list.append(data[y][x] + data[y][x-1] + data[y][x-2] + data[y][x-3])
            if y + 3 < len(data):
                list.append(data[y][x] + data[y+1][x] + data[y+2][x] + data[y+3][x])
            if y - 3 >= 0:
                list.append(data[y][x] + data[y-1][x] + data[y-2][x] + data[y-3][x])
            if x + 3 < len(data[y]) and y + 3 < len(data):
                list.append(data[y][x] + data[y+1][x+1] + data[y+2][x+2] + data[y+3][x+3])
            if x - 3 >= 0 and y - 3 >= 0:
                list.append(data[y][x] + data[y-1][x-1] + data[y-2][x-2] + data[y-3][x-3])
            if x + 3 < len(data[y]) and y - 3 >= 0:
                list.append(data[y][x] + data[y-1][x+1] + data[y-2][x+2] + data[y-3][x+3])
            if x - 3 >= 0 and y + 3 < len(data):
                list.append(data[y][x] + data[y+1][x-1] + data[y+2][x-2] + data[y+3][x-3])

            num = 0
            for xma in list:
                if xma == 'XMAS':
                    result += 1
                    num += 1
        if data[y][x] == 'A':
            list = []
            if x + 1 < len(data[y]) and y + 1 < len(data) and x - 1 >= 0 and y - 1 >= 0:
                list.append(data[y-1][x-1] + data[y][x] + data[y+1][x+1])
                list.append(data[y+1][x+1] + data[y][x] + data[y-1][x-1])
                list.append(data[y-1][x+1] + data[y][x] + data[y+1][x-1])
                list.append(data[y+1][x-1] + data[y][x] + data[y-1][x+1])

            if list.count('MAS') == 2:
                result2 += 1
            




print(result, result2)

def count_xmas(word_search):
    target = "XMAS"
    count = 0
    n = len(word_search)
    
    # 수평 및 역방향 수평 검색
    for row in word_search:
        count += row.count(target)  # 수평
        count += row[::-1].count(target)  # 역방향 수평

    # 수직 검색
    for col in range(len(word_search[0])):
        column = ''.join(row[col] for row in word_search)
        count += column.count(target)  # 수직
        count += column[::-1].count(target)  # 역방향 수직

    # 대각선 검색
    for r in range(n):
        for c in range(len(word_search[0])):
            # 오른쪽 아래 대각선
            if r + 3 < n and c + 3 < len(word_search[0]):
                diag = ''.join(word_search[r + i][c + i] for i in range(4))
                count += diag.count(target)
                count += diag[::-1].count(target)
                
            # 왼쪽 아래 대각선
            if r + 3 < n and c - 3 >= 0:
                diag = ''.join(word_search[r + i][c - i] for i in range(4))
                count += diag.count(target)
                count += diag[::-1].count(target)

    return count

print(count_xmas(data))
