n=int(input())
nlist=[0]*n
candy=[]
n0=0
for i in range(n):
    k=int(input())
    candy.append(k)
    if i%2==0:
        n0+=k
    else:
        n0-=k
nlist[0]=n0//2
for j in range(1,n):
    nlist[j]=candy[j-1]-nlist[j-1]
for i in nlist:
    print(i)
# n0+n1=k0
# n1+n2=k1 
# n2+n0=k2
# ....
# n0-n2=k0-k1
# n0+n2=k2
# 2n0=k0-k1+k2