# https://www.acmicpc.net/problem/1080
# 행렬
# 그리디 알고리즘 / 좌표마다 확인해나가며 원하는 값이 나올때까지 끝까지 진행

import sys


N, M = map(int, sys.stdin.readline().split())
mx1 = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
mx2 = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

def func(arr, px, py):
    for i in range(px, px+3):
        for j in range(py, py+3):
            arr[i][j] = 1-arr[i][j]
            
if mx1 == mx2:
    print(0)
else:
    count = 0       
    for i in range(N-2):
        for j in range(M-2):
            if mx1[i][j] != mx2[i][j]:
                func(mx1, i, j)
                count += 1

    for i in range(N):
        for j in range(M):
            if mx1[i][j] != mx2[i][j]:
                count = -1
                
    print(count)