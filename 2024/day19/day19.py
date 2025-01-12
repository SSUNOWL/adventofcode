from functools import cache


with open("2024/day19/day19.txt") as f:
    ls = f.read().strip().split("\n")

stripes, _, *patterns = ls
stripes = stripes.split(", ")


@cache
# 특정 인풋에 대한 함수의 결과값을 저장합니다. --> dp 이게 핵심;; 재귀함수에서 이걸 사용하면 같은 입력값이 들어간 경우에대해 금방출력가능
def is_possible(pattern, op):
    return not pattern or op(
        is_possible(pattern[len(stripe) :], op)
        for stripe in stripes
        if pattern.startswith(stripe)
    )

# 패턴(긴거)를 하나씩 던짐
# 패턴에 대해서 stripe로 시작하는게 있는지 확인
# 있다면 포함되는걸 제외하고 패턴에서 또다시 확인;
# 패턴이 끝나면 True
# any에서는 하나만 되면 True출력
# sum에서는 합산해서 알려줌

# Part 1 + 2
for op in any, sum:
    print(sum(is_possible(pattern, op) for pattern in patterns))