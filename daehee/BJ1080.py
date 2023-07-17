A=open(0).read().split();n,m=int(A[0]),int(A[1])
a,b,c,d=A[2:2+n],A[2+n:],[[0]*m for _ in range(n)],0
for i in range(n):
    for j in range(m):
        c[i][j]=int(a[i][j])^int(b[i][j])
        d+=c[i][j]
del A
if n<3 or m<3:print(-1 if d else 0)
else:
    T=0
    for i in range(n-2):
        for j in range(m-2):
            if c[i][j]:
                T+=1
                for u in range(3):
                    for v in range(3):
                        c[i+u][j+v]^=1
    for i in range(n):
        for j in range(m):
            if c[i][j]:T=-1;break
    print(T)