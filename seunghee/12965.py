import sys
N, K = map(int, sys.stdin.readline().strip().split(' '))
dp = [[0]* K for _ in range(N)]
data = []
for _ in range(N):
    a, b  = map(int, sys.stdin.readline().strip().split(' '))
    data.append((a,b))

for i, one in enumerate(data): # 행, 물품들
  W, V = one # 무게, 가치
  for j in (1, K+1): # 1~ 최대 무게
     if W <= K: # 버틸수 있는 무게임 6 =< 6
        dp[i][j] = max(V, max(dp[:][j-W])) #i를 포함했을때 무게
     else:
         dp[i][j] = dp[i-1][j]

         0 1 2 3 4 5 6 7
(6,13) 0 0 0 0 0 0 0 13 
(4,8)  1 0 0 0 0 8 8 13  14
(3,6)  2 0 0 0 6 6 6 6 8
(5,12) 3 0 0 0 0 0 12 
