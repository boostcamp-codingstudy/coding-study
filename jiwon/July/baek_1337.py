# https://www.acmicpc.net/problem/1337
# 올바른 배열
# 단순 set 문제

import sys

N = int(sys.stdin.readline().strip())
_list = set([int(sys.stdin.readline().strip()) for _ in range(N)])

min_len = 5
for num in _list:

    # 필요한 개수만 있는 것 중에서 얼마나 있나 전체에서 확인
    check = set(range(num, num+5))
    min_len = min(min_len, len(check-_list))

print(min_len)
