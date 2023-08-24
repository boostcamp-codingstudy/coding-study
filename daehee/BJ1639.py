*A,=map(int,list(input()))
n=len(A);l,f=0,0
for l in range(n,0,-1):
    for i in range(n-l+1):
        if l%2:continue
        c=i+l//2;a,b=sum(A[i:c]),sum(A[c:i+l])
        if a==b:f=1;break
    if f:break
print(l if f else 0)