n=int(input())
nlist=list(map(int,input().split()))
dp=[0]*(n+1)
for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i]=max(dp[i],dp[i-j]+nlist[j-1])
print(dp[n])
# print(d)
# [1,5,6,7]
#n=1: 1 = p1
#n=2: p2 또는 p1+dp[1] 중에 큰 것 = 5 = p2
#n=3: p1+dp[2] 또는 p2+dp[1] 또는 p3 중에 큰 것 = 7 == p2 + dp[1]
#n=4: p2*2 또는 p1*4 또는 p1*2+p2 또는 p3+p1 또는 p4 중에 큰 것 = 10 = p2*2 = dp[4] 
# [5,2,8,10]
#n=1: p1=5
#n=2: p2 또는 p1+p1 중에 큰 것 = 10 = p1*2 =dp[2]
#n=3: p2+p1 또는 p1*3 또는 p3 중에 큰 것 = 15 = p1*3 = dp[3] 
#n=4: p2*2 또는 p1*4 또는 ~~= p1*4 = 20 = p4 + dp[2]
