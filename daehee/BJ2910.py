A=list(map(int,open(0).read().split()))
N,A,D=A[0],A[2:],{}
for e in set(A):D[e]=[0,N]
for i,e in enumerate(A):
    D[e][0]+=1
    if D[e][1]==N:D[e][1]=i
A.sort(key=lambda e:(D[e][0],-D[e][1]),reverse=True)
for e in A:print(e,end=' ')