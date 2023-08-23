import math
a=open(0).read().split()
a=a[1:];d=0
n=eval('*'.join(a))
for e in a:d+=n//int(e)
g=math.gcd(n,d)
print(f'{n//g}/{d//g}')