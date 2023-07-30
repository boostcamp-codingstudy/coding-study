# # standard solution
# *A,=map(int,open(0).read().split())
# N,B,c,i=A[0],[[_+1,e]for _,e in enumerate(A[1:])],0,0
# for _ in range(N):
#     print(B[i][0],end=' ')
#     k,c,B[i][0]=B[i][1],0,0
#     while _<N-1:
#         i+=k//abs(k);i%=N
#         if B[i][0]:c+=k//abs(k)
#         if c==k:break

# the best solution
*A,=map(int,open(0).read().split())
B,i=[[_+1,e]for _,e in enumerate(A[1:])],0
for _ in range(A[0]):
    print(B[i][0],end=' ')
    t=B[i][1]
    if t>0:t-=1
    del B[i]
    if B:i+=t;i%=len(B)