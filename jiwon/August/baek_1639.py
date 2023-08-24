# https://www.acmicpc.net/problem/1639
# 행운의 티켓
# sliding window 알고리즘 문제, 인덱스를 옮겨가며 나올 수 있는 최대를 찾는 브루트포스 문제

import sys

ticket = list(map(int, sys.stdin.readline().strip()))
answer = 0

if len(ticket) >= 2:
    for idx in range(len(ticket)-1):
        left, right = 0, 0
        for i in range(len(ticket)//2):
            if idx-i < 0 or idx+1+i >= len(ticket):
                break
            left, right = left+ticket[idx-i], right+ticket[idx+1+i]
            if left == right:
                answer = max(answer, 2*(i+1))

print(answer)
