'''

'''
# 오답 RuntimeError(NameError)
import sys

def solution():
    N, M, d = *map(int, input().split()), {}
    # if N < 3: return print(0)
    n = N * (N - 1) * (N -2) // 6
    for i in range(N): d[i + 1] = []
    for _ in range(M):
        k, v = sys.stdin.readline().split()
        d[int(k)].append(int(v))
    bad = set()
    for k in list(d.keys()):
        if len(d[k]) > 0:
            for k1 in d[k]:
                for k2 in range(1, N + 1):
                    if k2 != k1 and k2 != k:
                        bad.add(frozenset([k, k1, k2]))

    print(n - len(bad))

solution()
