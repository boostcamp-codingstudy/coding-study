import sys

n, m = map(int, sys.stdin.readline().split())
mot = [list(map(int, sys.stdin.readline().split())) for i in range(m)]
cntl = [-1 for i in mot]
for idx, i in enumerate(mot):
    a, b = i[0], i[1]
    for j in mot:
        if (a in j) or (b in j):
            cntl[idx] += 1
print(n * (n - 1) // 2 - (n - 2) * m + sum(cntl) // 2)
