import itertools

# 집합 정의
집합 = {1, 2, 3, 4, 5, 6, 7, 8}

# 2개짜리 쌍 생성
쌍들 = list(itertools.combinations(집합, 2))

# 비복원 추출을 위한 모든 가능한 쌍 조합 생성
조합들 = []
for 쌍1 in 쌍들:
    남은_요소 = 집합 - set(쌍1)
    for 쌍2 in itertools.combinations(남은_요소, 2):
        남은_요소2 = 남은_요소 - set(쌍2)
        for 쌍3 in itertools.combinations(남은_요소2, 2):
            남은_요소3 = 남은_요소2 - set(쌍3)
            for 쌍4 in itertools.combinations(남은_요소3, 2):
                조합들.append((쌍1, 쌍2, 쌍3, 쌍4))

# 결과 출력
for 조합 in 조합들:
    print(조합)
print(len(조합들))


print([sorted(['lr', 'cd', 'pv', 'kg', 'zb'])])


seen = set()
for i in range(16777216, 1000000000):
    seen.add((i % 16777216) % 10)
print(seen)