# # standard solution using a dict for the graph
# from collections import deque
# *A,=map(int,open(0).read().split())
# m,n,r=A[:3];A=A[3:];C=[0]*(m+1);D=[]
# for _ in range(m+1):D+=[[]]
# for i in range(n):
#     k,v=A[2*i:2*i+2]
#     D[k]+=[v];D[v]+=[k]
# for V in D[1:]:V.sort()
# Q=deque([r]);o=1;C[r]=o
# while Q:
#     k=Q.popleft()
#     for v in D[k]:
#         if C[v]==0:C[v]=1;o+=1;C[v]=o;Q+=[v]
# for v in C[1:]:print(v)

# standard solution using a list for the graph
from collections import deque
*A,=map(int,open(0).read().split())
m,n,r=A[:3];A=A[3:];C=[0]*(m+1);D=[]
for _ in range(m+1):D+=[[]]
for i in range(n):
    k,v=A[2*i:2*i+2]
    D[k]+=[v];D[v]+=[k]
for V in D[1:]:V.sort()
Q=deque([r]);o=1;C[r]=o
while Q:
    k=Q.popleft()
    for v in D[k]:
        if C[v]==0:C[v]=1;o+=1;C[v]=o;Q+=[v]
for v in C[1:]:print(v)