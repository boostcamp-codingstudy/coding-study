import sys
from collections import deque

def bfs(graph, root):
    visited = [[0]*w for _ in range(h)]
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += = graph[n] - set(visited)
    return visited


xy = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오른, 아래, 왼, 위
while True:
    w, h = map(int, sys.stdin.readline().strip().split(' '))
    if w == 0 and h == 0:
        break
    # 지도 받음
    root = []
    for _ in range(h):
        root.append(map(int, sys.stdin.readline().strip().split(' ')))

    # 개수 세기
    # for i in range(w):
    #     for j in range(h):
    #         if root[i][j] == '1':
    #             for x, y in xy:
    #                 if (i+x >= 0 and i+x < w) and (j+y >= 0 and j+y < h):
    #                     if root[i+x][j+y] == '1':
    #                         root[i+x][j+y] = root[i][j] + 1

