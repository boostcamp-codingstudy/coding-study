# https://www.acmicpc.net/problem/28419
# 더하기
# 단순 구현 문제

import sys

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().split()))

if N == 3:
    if numbers[1] < numbers[0]+numbers[2]:
        answer = -1
    else:
        answer = numbers[1] - (numbers[0] + numbers[2])
else:
    odd = sum([n for i, n in enumerate(numbers) if i % 2])        # 홀수 번째
    even = sum([n for i, n in enumerate(numbers) if not i % 2])        # 홀수 번째

    answer = abs(odd-even)

print(answer)
