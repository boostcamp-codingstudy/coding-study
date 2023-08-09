# # standard solution but it timed out
# *A,=map(int,open(0).read().split())
# n,m,q=A[0:3];A,B=A[3:],[[0]*m for _ in range(n)]
# for k in range(q):
#     if A[3*k]==1:
#         r,v=A[3*k+1]-1,A[3*k+2]
#         for j in range(m):
#             B[r][j]+=v
#     elif A[3*k]==2:
#         c,v=A[3*k+1]-1,A[3*k+2]
#         for i in range(n):
#             B[i][c]+=v
# for b in B:print(*b)

# # faster solution
# *A,=map(int,open(0).read().split())
# n,m,q=A[0:3];A,R,C=A[3:],[0]*n,[0]*m
# for k in range(q):
#     t=3*k;i,u,v=A[t:t+3]
#     if i%2:R[u-1]+=v
#     else:C[u-1]+=v
# for r in R:
#     for c in C:
#         print(r+c,end=' ')
#     print()

# faster and shorter solution
*A,=map(int,open(0).read().split())
n,m,q=A[0:3];A,R,C=A[3:],[0]*n,[0]*m
for k in range(q):
    t=3*k;i,u,v=A[t:t+3]
    if i%2:R[u-1]+=v
    else:C[u-1]+=v
for r in R:print(*[r+c for c in C])