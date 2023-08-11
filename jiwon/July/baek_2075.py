# https://www.acmicpc.net/problem/2075
# N번째 큰 수
# heapq로 계속 정렬된 큐를 유지, 원하는 크기의 큐를 얻기 위해 계속 크기 조절

import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().strip())

board = []
for _ in range(N):
    for n in map(int, sys.stdin.readline().split()):
        heappush(board, n)
        if len(board) > N:      # 큐의 크기 조절
            heappop(board)

print(board[0])