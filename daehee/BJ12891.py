n,p,s=*map(int,input().split()),input()
r=*map(int,input().split()),;D,N,e={},0,0
for c in 'ACGT':D[c]=0
for i in range(n-p+1):
    if i:
        D[s[i-1]]-=1
        D[s[i+p-1]]+=1
    else:
        for i in range(p):D[s[i]]+=1
    d,e=list(D.values()),0
    for j in range(4):
        if d[j]<r[j]:e=1;break
    if e==0:N+=1
print(N)

# n,p,s=*map(int,input().split()),input()
# r=*map(int,input().split()),;D,d,N,e='ACGT',[0]*4,0,0
# for i in range(n-p+1):
#     if i:
#         d[D.index(s[i-1])]-=1
#         d[D.index(s[i+p-1])]+=1
#     else:
#         for i in range(p):d[D.index(s[i])]+=1
#     e=0
#     for j in range(4):
#         if d[j] < r[j]:e=1;break
#     if e==0:N+=1
# print(N)