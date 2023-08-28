*A,=map(int,open(0).read().split())
n,m=A[:2]
while n:
    D={}
    for b in A[2:2+n*m]:
        if D.get(b,0):D[b]+=1
        else:D[b]=1
    B=[k for k in sorted(D.keys(),key=lambda e:-D[e])]
    print(*sorted([e for e in B if D[e]==D[B[1]]]))
    A=A[2+n*m:]
    n,m=A[:2]