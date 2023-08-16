from math import gcd
n=int(input())
A=list(map(int,input().split()))
bunmo=1
bunza=0
def lcm(a,b):
    return a*b//gcd(a,b)
for i in range(n):
    bunmo=lcm(bunmo,A[i])

for i in range(n):
    bunza+=(bunmo//A[i])
gcd1=gcd(bunmo,bunza)
print(f'{bunmo//gcd1}/{bunza//gcd1}')

