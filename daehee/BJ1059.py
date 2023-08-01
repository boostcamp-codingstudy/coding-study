*A,=map(int,open(0).read().split())
L,S,n=A[0],[0]+A[1:-1],A[-1]
S.sort()
if n in S:print(0)
else:
    l=r=n
    for i in range(L):
        l,r=S[i],S[i+1]
        if l<n<r:break
    print((n-l)*(r-n)-1)