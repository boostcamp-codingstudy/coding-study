import sys
from math import gcd
N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

down = 1
up = 0

# 1/3, 1/2 -> 2/6, 3/6
for a in A:
    down *= a

for a in A:
    up += down//a
    
print(f"{down//gcd(down,up)}/{up//gcd(down,up)}")