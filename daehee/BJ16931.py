*A,=map(int,open(0).read().split())
n,m=A[:2];A=A[2:];s=2*n*m
k=max(A)
print(2*(n*m+n*k+m*k))