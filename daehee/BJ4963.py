'''

'''
# standard solution using BFS
import sys
input=sys.stdin.readline
D=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
def B(M,i,j,c):
    Q=[[i,j]]
    while Q:
        i,j=Q.pop(0)
        for d in D: 
            u,v=i+d[0],j+d[1]
            if -1<u<h and -1<v<w:
                if M[u][v]==1:M[u][v]+=c;Q+=[[u,v]]
                else:M[u][v]=-1     
while True:
    w,h=map(int,input().split())
    if h==0:break
    M=[list(map(int,input().split()))for _ in range(h)]
    c=1
    for i in range(h):
        for j in range(w):
            if M[i][j]==1:B(M,i,j,c);c+=1
    print(c-1)

# # standard solution using DFS 
# import sys
# input=sys.stdin.readline
# sys.setrecursionlimit(2500)
# D=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
# def B(M,i,j,c):
#     M[i][j]+=c
#     for d in D:
#         u,v=i+d[0],j+d[1]
#         if -1<u<h and -1<v<w:
#             if M[u][v]==1:B(M,u,v,c)
#             else:M[u][v]=-1
# while True:
#     w,h=map(int,input().split())
#     if h==0:break
#     M=[list(map(int,input().split()))for _ in range(h)]
#     c=1
#     for i in range(h):
#         for j in range(w):
#             if M[i][j]==1:B(M,i,j,c);c+=1
#     print(c-1)