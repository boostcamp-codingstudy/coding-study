import sys
from collections import Counter

input = sys.stdin.readline
n, m = map(int, input().split())
dna = [list(input().rstrip()) for i in range(n)]
cdlst = [[] for i in range(m)]
nwlst = []
for i in dna:
    cnt = 0
    for j in i:
        cdlst[cnt].append(j)
        cnt += 1
for cd in cdlst:
    nwlst.append(Counter(cd))

# print(nwlst)
newdna = []
for idx, i in enumerate(nwlst):
    a = sorted(nwlst[idx].items(), key=lambda item: (-item[1], item[0]))
    newdna.append(a[0][0])
ans = 0
for idx, i in enumerate(newdna):
    ans += n - nwlst[idx][i]
print("".join(newdna))
print(ans)
