# https://www.acmicpc.net/problem/1448
# 삼각형 만들기
# 단순 sliding window + 완전 탐색 문제 / combinations를 사용했다가 메모리 초과로 실패

import sys

N = int(sys.stdin.readline().strip())
straw = sorted([int(sys.stdin.readline().strip())
               for _ in range(N)], reverse=True)    # 내림차순 정렬

for idx in range(len(straw)-2):
    if straw[idx] < sum(straw[idx+1:idx+3]):
        answer = sum(straw[idx:idx+3])
        break
else:
    answer = -1

print(answer)
