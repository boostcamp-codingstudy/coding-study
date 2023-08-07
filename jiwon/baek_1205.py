# https://www.acmicpc.net/problem/1205
# 등수 구하기
# 데이터의 개수가 별로 없어서 일반적인 sort로도 문제 풀이 가능
# 데이터가 많아지면 bisect와 같은 이분탐색을 활용해야 할 듯

import sys

N, new_score, P = map(int, sys.stdin.readline().split())
if N == 0:      # 이미 등수에 아무도 없으면 내가 1등임
    print(1)
else:
    score = list(map(int, sys.stdin.readline().split()))
    if N == P and score[-1] >= new_score:       # 턱걸이에 걸렸는데 이미 같은애가 있으면 아웃
        print(-1)
    else:
        res = N + 1
        for i in range(N):      # 끝까지 가면 n+1이 최종값
            if score[i] <= new_score:       # 그 전에 걸리면 break
                res = i + 1
                break
        print(res)
