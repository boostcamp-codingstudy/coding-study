import heapq as hq
*A,=map(int,open(0).read().split())
n,A,B=A[0],A[1:],[]
for a in A:
    if a:hq.heappush(B,a)
    else:
        if B:print(hq.heappop(B))
        else:print(0)