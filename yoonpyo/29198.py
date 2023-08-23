n,m,k=list(map(int,input().split()))
S=[]
for i in range(n):
    S.append(input())
S.sort()
T=[]
for i in range(k):
    T+=S[i]
print(*sorted(T),sep='')