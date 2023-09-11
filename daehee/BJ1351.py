# # standard solution using DFS - time-out
# n,p,q=map(int,open(0).read().split())
# def B(k):
#     if k==0:return 1
#     return B(k//p)+B(k//q)
# print(B(n))

# # standard solution using BFS - memory limit exceeded
# from collections import deque as dq
# n,p,q=map(int,open(0).read().split())
# def B(n):
#     c=0
#     Q=dq([n])
#     while Q:
#         n=Q.popleft()
#         if n:Q+=[n//p,n//q]
#         else:c+=1
#     return c
# print(B(n))

# the best solution using dynamic programming
n,p,q=map(int,open(0).read().split());D={}
def B(k):
    if k==0:return 1
    if D.get(k,0):return D[k]
    else:D[k]=B(k//p)+B(k//q);return D[k]
print(B(n))
