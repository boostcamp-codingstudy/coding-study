# standard solution using DFS - recursion limit matters
import sys
sys.setrecursionlimit(10000)
*A,=map(int,open(0).read().split())
n,m,k=A[:3];A=A[3:];D=[[0,-1],[1,0],[0,1],[-1,0]]
M=[0]*m*n;t=0
def B(r,c,t):
    if M[m*r+c]:
        t+=1
        M[m*r+c]=0
        for d in D:
            u,v=r+d[0],c+d[1]
            if -1<u<n and -1<v<m:t=B(u,v,t)
    return t
for i in range(k):r,c=A[2*i:2*i+2];M[m*(r-1)+c-1]=1
for r in range(n):
    for c in range(m):t=max(B(r,c,0),t)
print(t)

# # standard solution using BFS
# from collections import deque
# *A,=map(int,open(0).read().split())
# n,m,k=A[:3];A=A[3:];D=[[0,-1],[1,0],[0,1],[-1,0]]
# M=[0]*m*n;t=0
# def B(r,c,t):
#     Q=deque([[r,c]])
#     while Q:
#         r,c=Q.popleft()
#         if M[m*r+c]:
#             t+=1;M[m*r+c]=0
#             for d in D:
#                 u,v=r+d[0],c+d[1]
#                 if -1<u<n and -1<v<m:
#                     if M[m*u+v]:Q.append([u,v])
#     return t
# for i in range(k):r,c=A[2*i:2*i+2];M[m*(r-1)+c-1]=1
# for r in range(n):
#     for c in range(m):t=max(B(r,c,0),t)
# print(t)