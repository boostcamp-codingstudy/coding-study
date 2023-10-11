# # standard solution - time limit exceeded
# R=open(0).readline
# n=int(R());P=[]
# for i in range(n):P+=[[*map(int,R().split())]]
# q=int(R())#;Q=[]
# for i in range(q):
#     k=float(R());f=0
#     for i in range(len(P)-1):
#         if P[i][0]<k<P[i+1][0]:
#             if P[i][1]<P[i+1][1]:f=1
#             elif P[i][1]>P[i+1][1]:f=-1
#             else:f=0
#             break
#     print(f)

# # standard solution 2
# R=open(0).readline
# n=int(R());P=[]
# for i in range(n):P+=[[*map(int,R().split())]]
# q=int(R());Q=[]
# for i in range(q):Q+=[[i,float(R())]]
# Q.sort(key=lambda e:e[1])
# A=[0]*q;i,j=0,0
# while 1:
#     if P[j][0]<Q[i][1]<P[j+1][0]:
#         f=P[j+1][1]-P[j][1]
#         if f>0:f=1
#         elif f<0:f=-1
#         A[Q[i][0]]=f
#         i+=1
#     else:j+=1
#     if i>q-1 or j>n-1:break
# for a in A:print(a)

# # standard solution 3 using binary search
# R=open(0).readline
# n=int(R());P=[]
# for i in range(n):P+=[[*map(int,R().split())]]
# q=int(R())
# for i in range(q):
#     k=float(R());s,e=0,n-1
#     while s+1<e:
#         m=(s+e)//2
#         if k>P[m][0]:s=m
#         else:e=m
#     f=P[e][1]-P[s][1]
#     if f>0:f=1
#     elif f<0:f=-1
#     print(f)

# the best solution
A=open(0).read().split();n=int(A[0]);A=A[1:];X=[];S=[];t=0
for i in range(n):x,y=A[2*i:2*i+2];X+=[int(x)];y=int(y);f=y-t;S+=[f//abs(f)if f else 0];t=y
q=int(A[2*n]);A=A[2*n+1:];Q=sorted(enumerate(map(float,A)),key=lambda e:e[1]);F=[0]*q;j=0
for i,k in Q:
    while X[j]<=k:j+=1
    F[i]=S[j]
print(*F,sep='\n')

# # hybrid solution
# R=open(0).readline
# n=int(R());P=[];t=0;S=[]
# for i in range(n):P+=[[*map(int,R().split())]]
# for _,y in P:f=y-t;S+=[f//abs(f)if f else 0];t=y
# q=int(R());Q=[]
# for i in range(q):Q+=[[i,float(R())]]
# Q.sort(key=lambda e:e[1])
# A=[0]*q;j=0
# for i,k in Q:
#     while P[j][0]<=k:j+=1
#     A[i]=S[j]
# print(*A,sep='\n')