# # standard solution
# *A,=map(int,open(0).read().split());N,M=A[0:2];B=[0,A[2]]
# for k in range(1,N):B+=[B[-1]+A[2+k]]
# for k in range(M):
#     t=2+N+2*k
#     print(B[A[t+1]]-B[A[t]-1])

# faster solution
from itertools import*
*A,=map(int,open(0).read().split());N,M=A[0:2]
*B,=accumulate(map(int,A[2:2+N]),initial=0)
for k in range(M):
    t=2+N+2*k
    print(B[A[t+1]]-B[A[t]-1])

# # the best solution
# from itertools import*
# Q=map(str.split,open(0).read().splitlines());next(Q)
# *A,=accumulate(map(int,next(Q)),initial=0)
# print(*([A[int(j)]-A[int(i)-1]for i,j in Q]),sep='\n')