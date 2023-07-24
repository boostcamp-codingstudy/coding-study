# https://www.acmicpc.net/problem/1051
# 숫자 정사각형
# 하나씩 좌표를 찾아가며 확인하는 브루트포스 문제

import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

maximum = 1
for i in range(N):      # 모든 좌표를 지나며 가장 큰 결과값 찾기
    for j in range(M):
        length = min(N-i, M-j)      # 가로/세로 중 짥은 길이를 확인
        for l in range(2,length+1):
            # 직접 좌표를 하나씩 확인해 보며 조건에 맞는지 확인
            if board[i][j] == board[i+l-1][j] and board[i][j] == board[i][j+l-1] and board[i][j] == board[i+l-1][j+l-1]:
                # print(i, j, l)
                maximum = max(maximum,l)
                
    if maximum > N-(i+2):       # 남은 애들이 만들 수 없는 상황이면 사전 종료
        break
    
print(maximum**2)