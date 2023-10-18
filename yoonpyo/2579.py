# 다이나믹 프로그래밍 dp
n=int(input())
dp=[0]*(n+1)
stairs=[]
for _ in range(n):
    stairs.append(int(input()))
dp[0]=stairs[0]
if n>=2:
    dp[1]=stairs[0]+stairs[1]
if n>=3:
    dp[2]=max(stairs[0]+stairs[2],stairs[1]+stairs[2])
    for i in range(3,n):
        dp[i]=max(stairs[i]+stairs[i-1]+dp[i-3],stairs[i]+dp[i-2])
print(dp[n-1])