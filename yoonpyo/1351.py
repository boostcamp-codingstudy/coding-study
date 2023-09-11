from collections import defaultdict
n,p,q=map(int,input().split())
dp=defaultdict(int)
# dp=[0]*(n+1)
dp[0]=1
def infinite(n):
    if dp[n]>0:
        return dp[n]
    dp[n]=infinite(n//p)+infinite(n//q)
    return dp[n]
print(infinite(n))
