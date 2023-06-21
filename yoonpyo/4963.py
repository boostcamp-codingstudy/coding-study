from collections import deque
# dx=[-1,1,0,0,-1,-1,1,1] #대각선까지 총 8방향
# dy=[0,0,-1,1,0,-1,1,-1,1]
dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]
def bfs(graph,x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=h or ny<0 or ny>=w:
                continue
            if graph[nx][ny]==0:
                continue
            elif graph[nx][ny]==1:
                graph[nx][ny]=0 # 방문 표시
                queue.append((nx,ny))

while True:
    count=0
    w,h=list(map(int,input().split()))
    if w==0 and h==0:
        break
    graph=[[0]*w for _ in range(h)]
    for i in range(h):
        graph[i]=list(map(int,input().split()))
    
    for x in range(h):
        for y in range(w):
            if graph[x][y]==1:
                bfs(graph,x,y)
                count+=1
    print(count)