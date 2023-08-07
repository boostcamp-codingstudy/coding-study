# # simple but slow solution
# import sys
# sys.setrecursionlimit(10000)
# D=[[1,0],[0,1],[0,-1],[-1,0]]

# def F(B,n,m,r,c):
#     if 0<=r<n and 0<=c<m:
#         if B[r][c]==1:
#             B[r][c]+=1
#             for d in D:F(B,n,m,r+d[0],c+d[1])

# for t in range(int(input())):
#     m,n,k=map(int,input().split())
#     B=[[0]*m for _ in range(n)]
#     for j in range(k):
#         c,r=map(int,input().split());B[r][c]=1
#     g=0
#     for r in range(n):
#         for c in range(m):
#             if B[r][c]==1:F(B,n,m,r,c);g+=1
#     del B;print(g)

# # the best solution using DFS
# import sys
# sys.setrecursionlimit(10000)
# *A,=map(int,open(0).read().split());i=1
# D=[[1,0],[0,1],[0,-1],[-1,0]]

# def F(B,n,m,r,c):
#     if 0<=r<n and 0<=c<m:
#         if B[r][c]==1:
#             B[r][c]=2
#             for d in D:F(B,n,m,r+d[0],c+d[1])

# for t in range(A[0]):
#     m,n,k=A[i:i+3]
#     B=[[0]*m for _ in range(n)]
#     for j in range(k):
#         p=i+3+2*j;c,r=A[p:p+2];B[r][c]=1
#     g=0
#     for r in range(n):
#         for c in range(m):
#             if B[r][c]==1:F(B,n,m,r,c);g+=1
#     i+=2*k+3;del B;print(g)

# the best solution using BFS
*A,=map(int,open(0).read().split());i=1
D=[[1,0],[0,1],[0,-1],[-1,0]]

def F(B,n,m,r,c):    
    Q=[[r,c]]
    B[r][c]=2#;s,e=0,1
    while Q:#s<e:
        r,c=Q.pop(0)#Q[s];s+=1
        for d in D:
            i,j=r+d[0],c+d[1]            
            if 0<=i<n and 0<=j<m:
                if B[i][j]==1:
                    B[i][j]=2
                    Q+=[[i,j]]#;e+=1

for t in range(A[0]):
    m,n,k=A[i:i+3]
    B=[[0]*m for _ in range(n)]
    for j in range(k):
        p=i+3+2*j;c,r=A[p:p+2];B[r][c]=1
    g=0
    for r in range(n):
        for c in range(m):
            if B[r][c]==1:F(B,n,m,r,c);g+=1
    i+=2*k+3;del B;print(g)