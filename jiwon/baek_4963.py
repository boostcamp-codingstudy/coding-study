# https://www.acmicpc.net/problem/4963
# 섬의 개수
# BFS/DFS 문제

import sys
from collections import deque
pos = [[0, 1],  [1, 1],   [1, 0],  [1, -1],
       [0, -1], [-1, -1], [-1, 0], [-1, 1]]


def bfs(p1, p2):
    dq = deque([[p1, p2]])
    my_map[p1][p2] = 0
    while dq:
        n1, n2 = dq.popleft()
        for p in pos:
            posh = n1+p[0]
            posw = n2+p[1]

            if 0 <= posh < H and 0 <= posw < W and my_map[posh][posw]:
                dq.append([posh, posw])
                my_map[posh][posw] = 0


while True:
    W, H = map(int, sys.stdin.readline().split())

    if W == 0 and H == 0:   # 종료 조건
        break

    my_map = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

    points = 0

    for n in range(H):
        for m in range(W):
            if my_map[n][m] == 1:
                bfs(n, m)
                points += 1

    print(points)
