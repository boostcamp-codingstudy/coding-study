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

# faster solution
*A,=map(int,open(0).read().split())
n,m,q=A[0:3];A,B=A[3:],[[0]*n,[0]*m]
for k in range(q):
    t=3*k;a,u,v=A[t:t+3]
    if a==1:B[0][u-1]+=v
    elif a==2:B[1][u-1]+=v
for r in B[0]:
    for c in B[1]:
        print(r+c,end=' ')
    print()