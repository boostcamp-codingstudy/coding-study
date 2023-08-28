*A,=map(int,open(0).read().split())
n,A,e,o=A[0],A[1:],0,0
for i,a in enumerate(A):
    if i%2:e+=a
    else:o+=a
if e>=o:print(e-o)
else:
    if n>3:print(o-e)
    else:print(-1)