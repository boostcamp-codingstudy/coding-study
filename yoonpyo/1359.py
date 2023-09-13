from itertools import combinations
n,m,k=map(int,input().split())
nlist=[i for i in range(1,n+1)]
cnt=0
for i in combinations(nlist,m):
    for j in combinations(nlist,m):
        if len(set(i)&set(j))>=k:
            cnt+=1
print(cnt/len(list(combinations(nlist,m)))**2)