import sys
sys.setrecursionlimit(10**7)

f = open("day13.txt", 'r')

d = []
while True:
    line = f.readline()
    if not line: break
    if line != '\n':
        spl = line.split('\n')[0]
        pl = spl.split(': ')[1]
        d.append(pl)

f.close()


data = []
for i in range(0, int(len(d) / 3)):
    
    xa = int(d[3 * i + 0].split('+')[1].split(',')[0])
    ya = int(d[3 * i + 0].split('+')[2])
    xb = int(d[3 * i + 1].split('+')[1].split(',')[0])
    yb = int(d[3 * i + 1].split('+')[2])
    xp = int(d[3 * i + 2].split('=')[1].split(',')[0])
    yp = int(d[3 * i + 2].split('=')[2])

    machine = {'A' : (xa, ya), 'B' : (xb, yb), 'Prize' : [xp, yp]}
    data.append(machine)

    
def push(mac):
    ans = set()
    prx = mac['Prize'][0]
    pry = mac['Prize'][1]

    print(mac)

    xa = mac['A'][0]
    xb = mac['B'][0]
    ya = mac['A'][1]
    yb = mac['B'][1]

    B = (pry * xa - ya * prx) / (yb * xa - ya * xb)
    A = (prx - xb * B) / xa

    #연립방정식의 해를 풀어보자
    

    if A.is_integer() and B.is_integer():
        ans.add((A, B))

    return ans
        
        
        
    
    
        
        

def solve(part2):
    res = 0
    for mac in data:
        if part2:
            mac['Prize'][0] += 10000000000000
            mac['Prize'][1] += 10000000000000
        ans = push(mac)
        token = 100000000000009999999999
        if  len(ans) > 0:
            for i in ans:
                now = i[0] * 3 + i[1] * 1
                if token > now:
                    token = now
            res += token
            
    return int(res)
                


        
print(solve(True))