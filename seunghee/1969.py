import sys
from collections import Counter
N, M = map(int, sys.stdin.readline().strip().split(' '))

s = [[] for i in range(4) for j in range(M)]
dna = {'A' : 0, 'T' : 1, 'G' :2 , 'C' : 3}

for _ in range(N):
    s = sys.stdin.readline().strip()
    
