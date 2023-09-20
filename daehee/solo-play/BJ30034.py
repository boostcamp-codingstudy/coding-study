import sys
r=sys.stdin.readline
r();A=r().split();r();B=r().split()
r();C=r().split();r();S=r()
for e in set(A+B)-set(C):S=S.replace(e,' ')
print(*S.split(),sep='\n')