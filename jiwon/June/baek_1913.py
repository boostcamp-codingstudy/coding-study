# https://www.acmicpc.net/problem/1913
# 달팽이
# 커서를 활용한 좌표 구하기 문제

import sys

N = int(sys.stdin.readline().strip())      # 7
order = int(sys.stdin.readline().strip())      # 35
matchpoint = []

matrix = [[0]*N for _ in range(N)]
cursor = [(1, 0), (0, 1), (-1, 0), (0, -1)]
xpos, ypos = 0, 0
flag = 0

for i in range(N*N, 0, -1):
    matrix[xpos][ypos] = i
    if i == order:
        matchpoint = [xpos+1, ypos+1]
    if not ((0 <= xpos+cursor[flag][0] <= N-1) and (0 <= ypos+cursor[flag][1] <= N-1)):
        flag = (flag+1) % len(cursor)
    elif matrix[xpos+cursor[flag][0]][ypos+cursor[flag][1]] != 0:
        flag = (flag+1) % len(cursor)
    xpos, ypos = xpos+cursor[flag][0], ypos+cursor[flag][1]

for m in matrix:
    for n in m:
        print(n, end=" ")
    print()

print(f"{matchpoint[0]} {matchpoint[1]}")
