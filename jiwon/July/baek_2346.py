# https://www.acmicpc.net/problem/2346
# 풍선 터뜨리기
# 원형큐를 활용한 문제 풀이 : dq.rotate()

import sys
from collections import deque

N = int(sys.stdin.readline().strip())
num_list = deque([(int(n), i+1)
                 for i, n in enumerate(sys.stdin.readline().split())])

result = []
while num_list:
    num, idx = num_list.popleft()
    # print(num, idx)

    result.append(str(idx))
    if num > 0:
        num_list.rotate(-(num-1))
    else:
        num_list.rotate(-num)

print(' '.join(result))
