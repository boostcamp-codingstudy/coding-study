# # largest memory occupation, shortest code
# *A,=map(int,open(0).read().split())
# n,m=A[:2]
# while n:
#     D={}
#     for b in A[2:2+n*m]:
#         if D.get(b,0):D[b]+=1
#         else:D[b]=1
#     B=sorted(D.keys(),key=lambda e:-D[e])
#     print(*sorted([e for e in B if D[e]==D[B[1]]]))
#     A=A[2+n*m:]
#     n,m=A[:2]

# # much smaller memory occupation, bit longer but faster code
# r=open(0).readline
# n,m=map(int,r().split())
# while n:    
#     D={}
#     for i in range(n):
#         for e in map(int,r().split()):
#             if D.get(e,0):D[e]+=1
#             else:D[e]=1
#     A=sorted(D.keys(),key=lambda e:-D[e])
#     print(*sorted([e for e in A if D[e]==D[A[1]]]))
#     n,m=map(int,r().split())

# the fastest code due to not using sorting
r=open(0).readline;k=10001
while 1:
    n,m=map(int,r().split())
    if n==0:break
    A=[0]*k;B=[]
    for _ in range(n):
        for e in map(int,r().split()):A[e]+=1
    M=max(A)
    for i in range(1,k):
        if A[i]==M:A[i]=0;break
    M=max(A)
    for i in range(1,k):
        if A[i]==M:B+=[i]
    print(*B)