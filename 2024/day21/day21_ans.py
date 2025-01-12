from functools import cache

def path(ss):
    
    (y,x), (Y,X) = [divmod('789456123_0A<v>'.find(t), 3) for t in ss] #divmod == (몫, 나머지) 0 == ^ ss== 출발지, 목적지
    S = '>' * (X - x) + 'v' * (Y - y) + '0' * (y - Y) + '<' * (x - X) # --> 차이에 따른 답에 따라서 이동해야하는 것
    return S if (3,0) in [(y,X), (Y,x)] else S[::-1] # --> 만약 _ ( 공백부분을 지나면 뒤집은 값 보냄)

@cache
def length(S, d):
    print(S, d)
    # for ss in zip('A' + S, S + 'A'):    #어차피 A ~~~~ A로 끝남 zip은 순서쌍을 만드는 함수
    #     print(ss) 
    if d < 0: 
        print(len(S) + 1)
        return len(S)+1
    return sum(length(path(ss), d-1) for ss in zip('A' + S, S + 'A'))   #실행순서는 dfs라고 봐야할듯 깊이우선 결국 리턴값을 길이로 하기때문에 cache가능




for r in 2, 25:
    print(sum(int(S[:3]) * length(S[:3], r) for S in open('2024/day21/day21.txt'))) # r == 반복횟수, S 는 입력값
