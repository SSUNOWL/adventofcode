from collections import defaultdict

import random
D = open("2024/day23/day23.txt").read().strip()

E = defaultdict(set)
for line in D.split('\n'):
    a,b, = line.split('-')
    E[a].add(b)
    E[b].add(a)
xs = sorted(E.keys())

p1 = 0
for i,a in enumerate(xs):
    for j in range(i+1, len(xs)):
        for k in range(j+1, len(xs)):
            b = xs[j]
            c = xs[k]
            if a in E[b] and a in E[c] and b in E[c]:
                if a.startswith('t') or b.startswith('t') or c.startswith('t'):
                    p1 += 1

best = None
for t in range(1000):
    random.shuffle(xs)
    clique = []
    for x in xs:
        ok = True
        for y in clique:
            if x not in E[y]:

                ok = False
        if ok:
            clique.append(x)
    if best is None or len(clique) > len(best):
        best = clique
        #print(t, len(best), ','.join(sorted(best)))
print(','.join(sorted(best)))
