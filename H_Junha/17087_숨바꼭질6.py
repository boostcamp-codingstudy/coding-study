import sys
from math import gcd

N,S = list(map(int,sys.stdin.readline().split())) #동생 수 N, 현재 위치 S
A = list(map(int,sys.stdin.readline().rstrip().split()))

step_list = []
for i in A:
    step_list.append(abs(i-S))
    
print(gcd(*step_list))
