# https://www.acmicpc.net/problem/1049
# 기타줄
# 단순 구현 문제

import sys

N, M = map(int, sys.stdin.readline().split())      # 4 2
min_lines, min_line = 999999999, 999999999

for _ in range(M):      # 각 패키지, 낱개 당 최소가격을 찾음
    l1, l2 = map(int, sys.stdin.readline().split())
    min_lines = min(min_lines, l1)
    min_line = min(min_line, l2)

tasks = [6]*(N//6) + [N % 6]

result = 0
for task in tasks:
    result += min(min_lines, min_line*task)

print(result)
