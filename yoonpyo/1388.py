def search(graph,i,j):
    if graph[i][j]=='-':
        graph[i][j]=0
        if j<len(graph[0])-1 and graph[i][j+1]=='-':
            search(graph,i,j+1)
            
        else:
            return
    elif graph[i][j]=='|':
        graph[i][j]=1
        if i<len(graph)-1 and graph[i+1][j]=='|':
            search(graph,i+1,j)
        else:
            return

n,m=map(int,input().split())
graph=[[0]*m for _ in range(n)]
for i in range(n):
    graph[i]=list(input())
cnt=0
for i in range(n):
    for j in range(m):
        if graph[i][j]=='-' or graph[i][j]=='|':
            search(graph,i,j)
            cnt+=1
print(cnt)
        
        
