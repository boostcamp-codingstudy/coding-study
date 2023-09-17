# standard solution using combinations
from itertools import combinations as C
*A,=map(int,open(0).read().split())
n,m=A[:2];A=A[2:];H=[];F=[]
for r in range(n):
    for c in range(n):
        t=A[r*n+c]
        if t==1:H+=[[r,c]]
        elif t==2:F+=[[r,c]]
S=[]
for f in C(F,m):
    s=0
    for i,h in enumerate(H):
        t=2*n
        for j in range(m):
            d=abs(h[0]-f[j][0])+abs(h[1]-f[j][1])
            if d<t:t=d
        s+=t
    S+=[s]
print(min(S))

# # the best solution
# *A,=map(int,open(0).read().split())
# n,m=A[:2];A=A[2:];H=[];F=[]
# for i in range(n):
#     for j in range(n):
#         if A[i*n+j]==2:F+=[(i,j)]
# for i in range(n):
#     for j in range(n):
#         if A[i*n+j]==1:
#             d=[]
#             for r,c in F:d+=[abs(r-i)+abs(c-j)]
#             H+=[d]
# C=[0]*len(F)
# def D():
#     I=[]
#     for i in range(len(F)):I+=[i]*C[i]
#     s=0
#     for h in H:
#         t=h[I[0]]
#         for i in I:
#             if h[i]<t:t=h[i]
#         s+=t
#     return s
# e=2*n*13
# def B(s,c):
#     global e
#     if c==m:
#         k=D()
#         if k<e:e=k
#     for i in range(s,len(F)):
#         if C[i]==0:C[i]=1;B(i,c+1);C[i]=0
# B(0,0)
# print(e)