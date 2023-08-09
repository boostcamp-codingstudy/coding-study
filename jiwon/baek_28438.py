# https://www.acmicpc.net/problem/28438
# 행렬 연산 (행렬 계산하기)
# 단순 구현 문제, 시간초과 고려하여 문제 풀기

import sys

N, M, Q = map(int, sys.stdin.readline().split())
log = [[0]*N, [0]*M]    # 0 : 행 계산, 1 : 열 계산

for _ in range(Q):
    op, line, cal = map(int, sys.stdin.readline().split())
    log[op-1][line-1] += cal

for i in range(N):
    for j in range(M):
        print(log[0][i]+log[1][j], end=" ")
    print()


'''
    # 시간초과
    # 일일이 연산을 진행하지 않고, 어차피 행/열마다 계산하는 거니까 따로 계산을 저장해두면 되지 않을까?
    # 각 행/열별로 연산한 것을 기록하고 한번에 표현하자
    
    import sys

    N, M, Q = map(int, sys.stdin.readline().split())
    mx = [[0]*M for _ in range(N)]

    for _ in range(Q):
        op, line, cal = map(int, sys.stdin.readline().split())

        # 행 계산
        if op == 1:
            for n in range(M):
                mx[line-1][n] += cal
        # 열 계산
        else:
            for n in range(N):
                mx[n][line-1] += cal

    for m in mx:
        print(' '.join(map(str, m)))

'''
