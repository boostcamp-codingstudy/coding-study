# # standard solution
# N,M=*map(int,input().split()),
# B,l=[[*map(int,list(input()))]for _ in range(N)],1
# for i in range(N):
#     for j in range(M):
#         n,r=min(N-i,M-j),B[i][j]
#         for k in range(n,0,-1):
#             p,q=i+k-1,j+k-1
#             if r==B[i][q]and r==B[p][j]and r==B[p][q]:
#                 if k>l:l=k;break
# print(l*l)

# the best solution
N,M=map(int,input().split());B=[input()for _ in range(N)]
for k in range(min(N,M),-1,-1):
    for i in range(N-k):
        for j in range(M-k):
            if B[i][j]==B[i][j+k]==B[i+k][j]==B[i+k][j+k]:
                exit(print((k+1)**2))

# # the shortest solution
# i,*a=open(0);n,m=map(int,i.split());r=range
# [[a[i][j]==a[i][j+k]==a[i+k][j]==a[i+k][j+k]and exit(print((k+1)**2))for i in r(n-k)for j in r(m-k)]for k in r(min(n,m),-1,-1)]