*A,=map(int,open(0).read().split())
n=A[0];A=A[1:];c=0
for i in range(n):c+=A[i]<=A[i+n]
print(c)