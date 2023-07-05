'''

'''
A=*map(int,open(0).read().split()),
N,A=A[0],A[1:]
C=[0]*N
for j in range(N):
    for i in range(j):
        if A[i]<A[j]:
            C[j]=max(C[i]+1, C[j])
print(max(C)+1 if N-1 else 0)