import sys

N, KIM, IM = list(map(int,sys.stdin.readline().split()))
cnt = 0
while KIM != IM:
    next = []
    cnt += 1
    for n in range(N):
        next.append(n//2+1)
        if n == KIM-1:
            KIM = n//2+1
        if n == IM-1:
            IM = n//2+1
    next = list(set(next))
    N = next[-1]

print(cnt)