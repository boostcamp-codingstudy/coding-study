n=int(input()) #상자개수
boxes=list(map(int,input().split()))
dp=[1]*(n)
for i in range(1,n):
    for j in range(i):
        if boxes[i]>boxes[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
##해설 참고 함