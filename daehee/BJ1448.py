*A,=map(int,open(0).read().split())
n=A[0];A=sorted(A[1:])[::-1];f=0
for i in range(n-2):
    if A[i]<A[i+1]+A[i+2]:f=1;break
print(sum(A[i:i+3])if f else -1)