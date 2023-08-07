from math import gcd
cha=[]
n,s=list(map(int,input().split()))
A=list(map(int,input().split()))
for i in A:
    cha.append(abs(s-i))
D=cha[0]
for i in range(1,n):
    D=gcd(D,cha[i])
print(D)