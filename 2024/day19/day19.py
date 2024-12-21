f = open("2024/day19/day19.txt", 'r')

towel_patterns_input = ""
designs_input = []
num = 0
while True:
    line = f.readline()
    if not line: break

    spl = line.split('\n')[0]
    if num == 0:
        towel_patterns_input = spl
    elif num >= 2:
        designs_input.append(spl)
    num += 1

    
f.close()

# print(towel_patterns_input, designs_input)

def count_ways(design, patterns, index=0):
    # 디자인의 끝에 도달한 경우
    if index == len(design):
        return 1
    
    total_ways = 0
    
    for pattern in patterns:
        # 현재 인덱스에서 패턴이 일치하는지 확인
        if design.startswith(pattern, index):
            # 일치하면 다음 인덱스로 재귀 호출
            total_ways += count_ways(design, patterns, index + len(pattern))
    
    return total_ways

def can_form_design(design, patterns):
    # 메모이제이션을 위한 딕셔너리
    memo = {}
    
    def helper(index):
        # 디자인의 끝에 도달했을 경우
        
        if index == len(design):
            return True
        if index in memo:
            return memo[index]
        
        # 가능한 패턴을 탐색
        for length in range(1, max_pattern_length + 1):
            if index + length <= len(design):
                segment = design[index:index + length]
                if segment in patterns:
                    if helper(index + length):
                        memo[index] = True
                        return True
        
        memo[index] = False
        return False

    return helper(0)

# 입력 받기

# 패턴과 디자인 분리
towel_patterns = towel_patterns_input.split(", ")
designs = designs_input

# 최대 패턴 길이 계산
max_pattern_length = max(len(pattern) for pattern in towel_patterns)


# 가능한 디자인 수 세기
possible_designs_count=0
res2 = 0
for design in designs:
    if can_form_design(design, towel_patterns):
        possible_designs_count += 1
        res2 += count_ways(design, towel_patterns)




# 결과 출력
print(f"가능한 디자인 수: {possible_designs_count}")

print(res2)