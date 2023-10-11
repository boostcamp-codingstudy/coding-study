# standard solution
*A,=map(int,open(0).read().split())
n,m=A[:2];A=A[2:];s=2*n*m+4*sum(A)
for r in range(n):
    for c in range(m):
        if r:s-=2*min(A[r*m+c],A[r*m-m+c])
        if c:s-=2*min(A[r*m+c],A[r*m+c-1])
print(s)