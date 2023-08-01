# https://www.acmicpc.net/problem/2578
# 빙고

import sys


# 철수의 빙고판
bingo = {}      # 빙고 번호 기록판
board = []      # 빙고 보드판
for i in range(5):
    numbers = list(map(int, sys.stdin.readline().split()))
    for j, number in enumerate(numbers):
        bingo[number] = [i, j]
    board.append(numbers)

# 사회자가 말한 순서
number = []
for _ in range(5):
    number.extend(sys.stdin.readline().split())


def check_bingo():
    check = 0
    # 가로 확인
    for i in range(5):
        if sum(board[i]) == 0:
            check += 1

    # 세로 확인
    for i in range(5):
        if board[0][i] + board[1][i] + board[2][i] + board[3][i] + board[4][i] == 0:
            check += 1

    # 대각선 확인(오/아래)
    tmp = 0
    for i in range(5):
        tmp += board[i][i]
    if tmp == 0:
        check += 1

    # 대각선 확인(오/위)
    tmp = 0
    for i in range(5):
        tmp += board[i][4-i]
    if tmp == 0:
        check += 1

    return check >= 3


idx = 0
while number:
    now = int(number[idx])
    x, y = bingo[now]
    board[x][y] = 0     # 부른 곳은 0으로 바꾸기
    if check_bingo():
        break
    idx += 1

print(idx+1)
