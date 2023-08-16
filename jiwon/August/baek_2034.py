# https://www.acmicpc.net/problem/2034
# 반음
# 나머지 연산을 통한 구현 문제

import sys

n = int(sys.stdin.readline().strip())
play = [int(sys.stdin.readline().strip()) for _ in range(n)]

piano = {0: "C", 2: "D", 4: "E", 5: "F", 7: "G", 9: "A", 11: "B"}

result = []

for k in piano.keys():
    now = k
    start = piano[k]
    for p in play:
        now = (now+p) % 12
        if now not in piano.keys():
            break
    else:
        result.append([start, piano[now]])

[print(*r) for r in sorted(result, key=lambda x: (x[0], x[1]))]
