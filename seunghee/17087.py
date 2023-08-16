import sys
from math import gcd
N, S = sys.stdin.readline().split(' ')
data  = list(sys.stdin.readline().split(' '))

d = [] # S와 거리차이 담음

for w in data:
    d.append(abs(int(S) - int(w)))

# 최대공약수 구해서 print
if len(d) == 1:
    print(d[0])
else:
    ans = gcd(*d)
    print(ans)

