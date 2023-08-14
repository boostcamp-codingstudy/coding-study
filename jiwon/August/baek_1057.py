# https://www.acmicpc.net/problem/1057
# 토너먼트
# 이진수 활용 문제, 나머지 연산을 사용한 조건 구현 문제

import sys

N, kim, im = map(int, sys.stdin.readline().split())
kim, im = kim-1, im-1

answer = 1
while N:
    if kim//2 == im//2:
        break
    kim, im = kim//2, im//2
    answer += 1
    N = N//2 + N % 2

print(answer)
