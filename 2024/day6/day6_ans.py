import sys
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else '6.in'
p1 = 0
p2 = 0
D = open('2024/day6/day6_input.txt').read().strip()

G = D.split('\n')
R = len(G)
C = len(G[0])
for r in range(R):
    for c in range(C):
        if G[r][c] == '^':
            sr,sc = r,c
block = set()

for o_r in range(R):
    for o_c in range(C):
        r,c = sr,sc
        d = 0 # 0=up, 1=right, 2=down, 3=left
        SEEN = set()
        SEEN_RC = set()
        while True:
            if (r,c,d) in SEEN:
                block.add((o_c, o_r))
                p2 += 1
                break
            SEEN.add((r,c,d))
            SEEN_RC.add((r,c))
            dr,dc = [(-1,0),(0,1),(1,0),(0,-1)][d]
            rr = r+dr
            cc = c+dc
            if not (0<=rr<R and 0<=cc<C):
                if G[o_r][o_c]=='#':
                    p1 = len(SEEN_RC)
                break
            if G[rr][cc]=='#' or rr==o_r and cc==o_c:
                d = (d+1)%4
            else:
                r = rr
                c = cc

print(p1)
print(p2)
print(block)