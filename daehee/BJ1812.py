*A,=map(int,open(0).read().split())
n=A[0];A=A[1:];B=[0]*n;s=0
for i,a in enumerate(A):s+=(-1)**i*a
B[0]=s//2
for i in range(n-1):B[i+1]=A[i]-B[i]
for b in B:print(b)