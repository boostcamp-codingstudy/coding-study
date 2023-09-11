'''

'''
# # 오답 RuntimeError(NameError)
# import sys
# def solution():
#     N, M, d, n = *map(int, input().split()), {}, 0
#     if N < 3: return print(0)
#     else: n = N * (N - 1) * (N -2) // 6
#     for i in range(N): d[i + 1] = []
#     for _ in range(M):
#         k, v = sys.stdin.readline().split()
#         d[int(k)].append(int(v))
#     bad = set()
#     for k in list(d.keys()):
#         if len(d[k]) > 0:
#             for k1 in d[k]:
#                 for k2 in range(1, N + 1):
#                     if k2 != k1 and k2 != k:
#                         bad.add(frozenset([k, k1, k2]))
#     print(n - len(bad))
# solution()

# # 오답 memory limit exceeded
# import sys
# input=sys.stdin.readline
# n,m,D,c=*map(int,input().split()),{},0
# if n<3:print(0)
# else:
#     c=n*(n-1)*(n-2)//6
#     for _ in range(m):
#         k,v=map(int,input().split())
#         if D.get(k,0):D[k]+=[v]
#         else:D[k]=[v]
#     B=set()
#     for k in D.keys():
#         if len(D[k]):
#             for k1 in D[k]:
#                 for k2 in range(1,n+1):
#                     if k2 not in[k,k1]:
#                         B.add(frozenset([k,k1,k2]))
#     print(c-len(B))

# # standard solution
# import sys
# input=sys.stdin.readline
# n,m=map(int,input().split());D=[]
# if n<3:print(0)
# else:
#     for _ in range(n+1):D+=[[]]
#     for _ in range(m):
#         k,v=map(int,input().split())
#         D[k]+=[v];D[v]+=[k]
#     # for d in D:d.sort();print(d)
#     c=0
#     for i in range(1,n+1):
#         for j in range(i+1,n+1):
#             if j in D[i]:continue
#             for k in range(j+1,n+1):
#                 if k in D[i]:continue
#                 if k in D[j]:continue
#                 c+=1
#     print(c)

# # standard solution 2
# import sys
# input=sys.stdin.readline
# n,m=map(int,input().split())
# D=[[0]*(n+1) for _ in range(n+1)]
# if n<3:print(0)
# else:
#     for _ in range(m):
#         k,v=map(int,input().split())
#         D[k][v]=1;D[v][k]=1
#     c=0
#     for i in range(1,n+1):
#         for j in range(i+1,n+1):
#             for k in range(j+1,n+1):
#                 if D[i][j]or D[j][k]or D[k][i]:continue
#                 c+=1
#     print(c)

# the best solution
*A,=map(int,open(0).read().split())
n,m=A[:2];A=A[2:];c=n*(n-1)*(n-2)//6
B=[set()for _ in range(n+1)]
for i in range(m):
    k,v=A[2*i:2*i+2]
    c-=n-2-len(B[k]|B[v])
    B[k].add(v);B[v].add(k)
print(c)