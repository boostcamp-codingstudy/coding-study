def DFS(D, i):
    if C[i - 1]: return
    C[i - 1] = 1
    print(i, end=' ')
    if len(D[i]):
        for j in D[i]: DFS(D, j)

def BFS(D, i):
    L = [i]
    C[i - 1] = 1
    while len(L):
        i = L.pop(0)
        print(i, end=' ')
        if len(D[i]):
            for j in D[i]:
                if C[j - 1] == 0:
                    L.append(j)
                    C[j - 1] = 1

N, M, V = map(int, input().split())
D, C = {}, [0] * N
for n in range(N): D[n + 1] = []
for _ in range(M):
    i, j = map(int, input().split())
    D[i].append(j)
    D[j].append(i)
for n in range(N):
    D[n + 1].sort()
DFS(D, V)
print()
C = [0] * N
BFS(D, V)