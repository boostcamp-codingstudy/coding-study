n=int(input())
tp=[]
for i in range(n):
    tp.append(list(map(int,input().split())))
dp=[0]*(n+1)
for i in range(n-1,-1,-1):
    if tp[i][0]+i>n: # i번째 날부터 남은 날짜가 t일보다 적으면
        dp[i]=dp[i+1] # 상담 안함(이익 그대로 유지)
    else: # 그렇지 않으면
        dp[i]=max(dp[i+1],tp[i][1]+dp[i+tp[i][0]])
        # 상담을 안하는 것과 i번째 날에 상담해서 얻는 이익 중 큰 것
print(dp[0])
