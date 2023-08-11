# https://www.acmicpc.net/problem/11052
# 카드 구매하기
# knapsack 유사 문제, 바로 dp로 넘어가도 됨

import sys

N = int(sys.stdin.readline().strip())      # 4
points = [0]+list(map(int, sys.stdin.readline().split()))       # 1 5 6 7

for n in range(2, N+1):
    comb = set([tuple(sorted([i, n-i]))
                for i in range(n+1)])    # (1, 1), (0, 2)
    maxnum = 0
    for c in comb:
        num = points[c[0]] + points[c[1]]
        maxnum = max(num, maxnum)
    points[n] = maxnum

print(points[N])
