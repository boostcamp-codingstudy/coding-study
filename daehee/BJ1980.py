n,m,t=map(int,open(0).read().split())
n,m=(n,m)if n<m else(m,n);A=[];f=0
for i in range(t+1):
    if f:break
    a=t-i
    for j in range(a//n+1):
        b=a-n*j
        if b%m==0:A+=[[j+b//m,i]];f=1
print(*A[-1])