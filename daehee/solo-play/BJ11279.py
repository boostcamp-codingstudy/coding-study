import heapq as hq
*A,=map(int,open(0).read().split())
n,A,B=A[0],A[1:],[]
for e in A:
    if e:hq.heappush(B,-e)
    else:
        if B:print(-hq.heappop(B))
        else:print(0)