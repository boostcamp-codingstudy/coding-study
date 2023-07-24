# correct but slow
# *A,=map(int,open(0).read().split())
# N,K=A[0:2];B=A[2:]
# for i in range(N):B+=[[B[2*i],B[2*i+1]]]
# B,D=B[2*N:],[0]*(K+1)
# for w,v in B:
#     for i in range(K,w-1,-1):
#         D[i]=max(D[i-w]+v,D[i])
# print(D[K])

# correct but timeout
# def D(w,v,i):
#     if w>K:return v-B[i][1]
#     M=v
#     for j in range(i+1,N):
#         t=D(w+B[j][0],v+B[j][1],j)
#         if t>M:M=t
#     return M

# *A,=map(int,open(0).read().split())
# N,K=A[0:2];B=A[2:]
# for i in range(N):B+=[[B[2*i],B[2*i+1]]]
# B=sorted(B[2*N:],key=lambda e:(e[0],-e[1]))
# print(D(0,0,-1))

# best solution
*A,=map(int,open(0).read().split())
N,K=A[0:2];B=A[2:]
for i in range(N):B+=[[B[2*i],B[2*i+1]]]
B,D=sorted(B[2*N:])[::-1],{0:0}
for w,v in B:
    T={}
    for p,m in D.items():
        if D.get(v+p,K+1)>(w+m):T[v+p]=w+m
    D.update(T)
print(max(D))