# https://www.acmicpc.net/problem/1347
# 미로 만들기
# 음수도 나머지 연산 가능, 로그를 남겨 좌표 관리

import sys

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

_ = int(sys.stdin.readline())       # 입력 수
commands = sys.stdin.readline()     # 입력 텍스트

direction = 2       # 현재 방향
x_list = [0]
y_list = [0]
for command in commands:
    if command == 'L':      # 반시계로 회전
        direction = (direction - 1) % 4
    elif command == 'R':    # 시계로 회전
        direction = (direction + 1) % 4
    elif command == 'F':    # 방향으로 이동
        x, y = x_list[-1], y_list[-1]
        nx, ny = x + dx[direction], y + dy[direction]
        x_list.append(nx)
        y_list.append(ny)

# 범위 구하기
max_x, min_x, max_y, min_y = max(x_list), min(x_list), max(y_list), min(y_list)
N, M = max_x - min_x + 1, max_y - min_y + 1
start_x, start_y = abs(min_x), abs(min_y)

# 지나간 거리 기록
board = [['#'] * M for _ in range(N)]
for x, y in zip(x_list, y_list):
    board[start_x + x][start_y + y] = '.'

# 출력
for b in board:
    print(''.join(b))
