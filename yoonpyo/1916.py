import heapq
import sys
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
distance=[int(1e9)]*(n+1) # 최단거리 테이블 무한으로 초기화
for _ in range(m):
    start,end,price=map(int,sys.stdin.readline().split())
    graph[start].append((price,end))
s,e=map(int,sys.stdin.readline().split())

def dijkstra(s):
    q=[]
    heapq.heappush(q,(0,s))
    distance[s]=0
    while q:
        d,s=heapq.heappop(q)
        if distance[s]< d:
            continue
        for price,end in graph[s]: # end, price
            now_d=d+price
            if distance[end]>now_d:
                heapq.heappush(q,(now_d,end))
                distance[end]=now_d

dijkstra(s) # 출발도시에서 출발
print(distance[e]) #도착 도시에서의 최소 비용