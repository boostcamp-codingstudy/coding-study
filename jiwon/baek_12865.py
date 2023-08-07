# https://www.acmicpc.net/problem/12865
# 평범한 배낭
# 대표적인 knapsack 문제(dp)

import sys

N, K = map(int, sys.stdin.readline().split())
backpacks = [[0,0]]+sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key = lambda x: x[0])

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]      # dp 초기값

for i, backpack in enumerate(backpacks[1:]):
    for v in range(K+1):
        weight, value = backpack        # 무게, 가치

        if v < weight:      # 가방 무게가 해당 경우에서 가능하지 않으면
            dp[i+1][v] = dp[i][v]
        else:               # 이전 데이터들을 기반으로 가능한지 확인
            dp[i+1][v] = max(dp[i][v], dp[i][v-weight] + value)

print(dp[N][K])