from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(graph,x,y):
    queue=deque()
    queue.append((x,y))
    visited = [[0]*len(graph[0]) for _ in range(len(graph))]
    visited[x][y] = 1
    
    while queue:
        x,y=queue.popleft()
        if graph[x][y]=='G':
            return visited[x][y]
        for i in range(4):
            nx,ny=x,y
            while True: # 부딪힐 때까지...
                nx=nx+dx[i]
                ny=ny+dy[i]
                if nx<0 or ny<0 or nx>=len(graph) or ny>=len(graph[0]): # 범위 벗어나면
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                if 0<=nx<len(graph) and 0<=ny<len(graph[0]) and graph[nx][ny]=='D': #장애물 만나면
                    nx -= dx[i] #장애물 바로 전칸
                    ny -= dy[i] #장애물 바로 전칸
                    break
            if not visited[nx][ny]:
                visited[nx][ny]=visited[x][y]+1 # 움직임 횟수
                queue.append((nx,ny))
    return -1
def solution(board):
    answer = 0
    graph=[]
    for i in board:
        graph.append(list(i))
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j]=='R':
                answer=bfs(graph,i,j)
    if answer==-1:
        return answer
    else:
        return answer-1