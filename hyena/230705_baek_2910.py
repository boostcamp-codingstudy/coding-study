# https://www.acmicpc.net/problem/2910
# done 

import sys

num, max_num = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
# print(arr)

order = [] # 순서
count = {} # 몇번 나왔는가
for n in arr:
    if n not in order:
        order.append(n)
        count[str(n)] = 1
    else:
        count[str(n)] += 1
# print(order)
# print(count)

key_sorted = dict(sorted(count.items(), key=lambda x: (x[1], order), reverse=True))
# print(key_sorted)

result = []
for key, value in key_sorted.items():
    for _ in range(value):
        result.append(int(key))
    # result.append(int(key) for _ in range(value))
# print(result)
print(*result)