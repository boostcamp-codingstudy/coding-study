from collections import deque
import sys

def dfs(que):
    while que:
        x,y = que.popleft()
        Imap[x][y] = 0
        for d in direction:
            nx = x+d[0]
            ny = y+d[1]
            if nx >= 0 and ny >= 0 and nx < H and ny < W:
                if Imap[nx][ny] == 1:
                    que.append([nx ,ny])

W, H = -1,-1

while True:
    W,H = list(map(int,sys.stdin.readline().split()))
    if (W == 0 and H == 0) or (W > 50 and H > 50):
        break  
    else:
        Imap = []
        for i in range(H):
            Imap.append(list(map(int,sys.stdin.readline().split())))
            
        # 12시부터 시계방향으로 8가지의 방향
        direction = [[1,0],[1,1],[-1,0],[-1,1],[1,-1],[-1,-1], [0,1],[0,-1]] #[-1,-1]
        result = 0
        # 1은 땅, 0 은 바다
        for i in range(H):
            for j in range(W):
                if Imap[i][j] == 1:
                    start = [i,j]
                    que = deque([start])
                    dfs(que)
                    #DFS
                    
                    result += 1
        print(result)