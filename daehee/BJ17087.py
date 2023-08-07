# standard solution
import math
*A,=map(int,open(0).read().split())
N,S=A[0:2];A=A[2:];B=[]
for e in A:B+=[S-e]
print(math.gcd(*B))

# # standard solution 2 - slower
# import math
# *A,=map(int,open(0).read().split())
# N,S=A[0:2];A=A[2:];B=S-A[0]
# for e in A:B=math.gcd(abs(S-e),B)
# print(B)