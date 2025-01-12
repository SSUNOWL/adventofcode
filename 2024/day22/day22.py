import math
import itertools



f = open("2024/day22/day22.txt", 'r')

data = []
while True:
    line = f.readline()
    if not line: break

    spl = line.split('\n')[0]
    data.append(int(spl))
    
f.close()


def mix(value, secret):
    return value ^ secret

def prune(secret):
    return secret % 16777216

def one(secret):
    value = secret * 64
    secret = mix(value, secret)
    return prune(secret)
def two(secret):
    value = math.floor(secret / 32)
    secret = mix(value, secret)
    return prune(secret)
def three(secret):
    value = secret * 2048
    secret = mix(value, secret)
    return prune(secret)

def change(secret):
    secret = one(secret)
    secret = two(secret)
    return three(secret)


res1 = 0
buyer = []
prices = []
SCORE = {}
for secret in data:
    
    epoch = 2000
    al = []
    updown = [0]
    price = [secret % 10]
    seen = set()
    for i in range(epoch):

        tmp = change(secret)
        updown.append(tmp % 10 - secret % 10)
        price.append(tmp % 10)
        if len(updown) >= 4:
            ke = (updown[-4], updown[-3], updown[-2], updown[-1])
            if ke not in seen:
                seen.add(ke)
                if ke in SCORE.keys():
                    SCORE[ke] += tmp % 10
                else:
                    SCORE[ke] = tmp % 10

        secret = tmp

    res1 += secret
    buyer.append(updown)
    prices.append(price)

# price의 변화(buyer값의 4개)가 겹치는 수가 많은 4개의 숫자를 구하고
# 그떄의 바나나의 개수를 더해
# 이론상 완벽했는데;;; 너무 오래걸림
# 그냥 변위로 나오는 값이 처음으로 나온 것은 score에 추가해줌
print(res1)
print(max(SCORE.values()))
  
# def chl(seq):
#     res = 0
#     for i in range(len(buyer)):
        
#         idx = buyer[i].find(seq)
#         if idx < 0:
#             continue 
#         elif buyer[i][idx -1 : idx + len(seq)] == '-' + seq:
#             continue
#         minus = buyer[i][:idx + len(seq) - 1].count('-')
#         print(prices[i][idx + len(seq) - 1 - minus])
#         res += prices[i][idx + len(seq) - 1 - minus]
#     return res
# vary = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9]
# res2 = 0
# # for i in reversed(list(itertools.permutations(vary, 4))):
# #     num = 0
# #     flag = False

# #     for j in i:
# #         num += j
# #         if -10 > num and num > 10:
# #             flag = True
# #             break
# #     if not flag:
# #         seq = ''
# #         for chra in i:
# #             seq += str(chra)
# #         n = chl(seq)
# #         if res2 < n:
# #             res2 = n
# #             print(seq, res2)
# print(res2)
# print(chl('02-23'))
# print(chl('20-12'))