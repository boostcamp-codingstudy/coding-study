# https://www.acmicpc.net/problem/1052
# 물병
# 이진수 문자열 + 그리디 알고리즘 / 인덱스의 위치를 잘 확인해볼 필요가 있음

import sys

N, K = map(int, sys.stdin.readline().split())
        
answer = 0 
while bin(N)[2:].count('1') > K:
    cal_idx = bin(N)[::-1].index('1')
    answer += 2**cal_idx
    N += 2 **cal_idx
    
print(answer)