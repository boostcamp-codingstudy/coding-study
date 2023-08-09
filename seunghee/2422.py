import sys
from itertools import combinations
n,m = map(int, sys.stdin.readline().strip().split(' '))

no_comb = []
for _ in range(m):
    x, y = map(int, sys.stdin.readline().strip().split(' '))
    no_comb.append((x, y))

icreams = [x+1 for x in range(n)]
combs = combinations(icreams, 3)

for comb in combinations(icreams, 3):
    if comb[]
ans = 0
no_cnt = 0
for comb in combs:
    for no in no_comb:
        if len(set(comb) - set(no)) == len(comb) - len(no):
            no_cnt += 1
            break
print(len(list(combs)) - no_cnt)