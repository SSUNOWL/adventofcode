
f = open("day11.txt", 'r')

d = dict()
while True:
    line = f.readline()
    if not line: break
    spl = line.split(' ')
    for appart in spl:
        if appart in d.keys():
            d[appart] += 1
        else:
            d[appart] = 1


f.close()

res =  []
def blink(nums, rep, now):
    num = dict()

    for i in nums.keys():
        if i == '0':
            if '1' in num.keys():
                num['1'] += nums[i]
            else:
                num['1'] = nums[i]
            continue
        elif len(i) % 2 == 0:
            if i[0:len(i) // 2] in num.keys():
                num[i[0:len(i) // 2]] += nums[i]
            else:
                num[i[0:len(i) // 2]] = nums[i]
            if str(int(i[len(i) // 2 :])) in num.keys():
                num[str(int(i[len(i) // 2 :]))] += nums[i]
            else:
                num[str(int(i[len(i) // 2 :]))] = nums[i]
            continue
        else:
            if str(int(i) * 2024) in num.keys():
                num[str(int(i) * 2024)] += nums[i]
            else:
                num[str(int(i) * 2024)] = nums[i]
    now +=1 

    if rep == now:
        global res
        res = num
        return num
    else:
        return blink(num, rep, now)

    

def solve(part2):
    res.clear()
    blink(d, 75, 0)
    result = 0
    for i in res.values():
        result += i
    
    return result

print(solve(False))
