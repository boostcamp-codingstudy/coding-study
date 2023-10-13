n=int(input())
graph=[[0]*n for _ in range(n)]
t=0
for i in range(n):
    graph[i]=list(map(str,input().split()))
    t+= graph[i].count('T')
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        while 0<=nx<n and 0<=ny<n or graph[nx][ny]!='O':
            if graph[nx][ny]=='S': # 이동하다가 S가 있으면
                return True
            else: # S가 없으면 계속 탐색
                nx+=dx[i]
                ny+=dy[i]
    return False

def solution(cnt): # 방해물 설치할 수 있는 모든 경우 찾기
    global result
    if cnt==3: # 방해물을 3개 설치하면 
        answer=0 # 초기화 
        for i in range(n):
            for j in range(n):
                if graph[i][j]=='T': # T에서 탐색 시작
                    if bfs(i,j)==False: # 탐색하는데 S를 못만나면
                        answer+=1
        if answer==t:
            result=True
        return
    for i in range(n):
        for j in range(n):
            if graph[i][j]=='X':
                graph[i][j]='O' # 방해물 설치해보고
                cnt+=1
                solution(cnt) # 탐색해보고
                graph[i][j]='X' # 원위치
                cnt-=1

result=False
solution(0)
if result==True:
    print("YES")
else:
    print("NO")


# def isT(x,y):
#     if 'S' in graph[x] and 'O' not in graph[x]:
#         if graph[x].index('T')<graph[x].index('S') and graph[x][y+1]=='X':
#             graph[x][y+1]='O'
#         elif graph[x].index('T')>graph[x].index('S') and graph[x][y-1]=='X':
#             graph[x][y-1]='O'
#         return False
#     elif 'S' in graph[x] and 'O' in graph[x]:
#         return True
# def isT2(x,y):
#     col=list(zip(*graph))[y]
#     if 'S' in col and 'O' not in col:
#         if col.index('T')< col.index('S') and graph[x+1][y]=='X':
#             graph[x+1][y]='O'
#         elif col.index('T')>col.index('S') and graph[x-1][y]=='X':
#             graph[x-1][y]='O'
#         return False
#     elif 'S' in col and 'O' in col:
#         return True