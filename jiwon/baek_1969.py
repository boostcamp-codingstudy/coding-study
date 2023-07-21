# https://www.acmicpc.net/problem/1969
# DNA
# 단순 Counter + 정렬 문제

import sys
from collections import Counter
N, M = map(int, sys.stdin.readline().split())
dna = [list(sys.stdin.readline().strip()) for _ in range(N)]

# 각 글자를 앞에 부터 하나씩 따와서 정렬하고 하나씩 추리면 됨
text, hd = "", 0
for i in range(M):
    _list = []

    for d in dna:
        _list.append(d[i])

    output = sorted(Counter(_list).most_common(),
                    key=lambda x: (-x[1], x[0]))[0]
    text += output[0]
    hd += (N - output[1])

print(text)
print(hd)
