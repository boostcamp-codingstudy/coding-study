import math
*A,=map(int,open(0).read().split())
n=A[0];A=sorted(A[1:]);B=[];c=0
for i in range(n-1):B+=[A[i+1]-A[i]]
g=math.gcd(*B)
for b in B:c+=(b-g)//g
print(c)