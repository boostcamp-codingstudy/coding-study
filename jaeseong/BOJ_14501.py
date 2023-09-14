import sys

sys.stdin = open('input.txt')

n = int(input())

answer = [(0,0)]

for day in range(1,n+1):
    time, price = map(int,input().split())

    answer.append((time,price))
 
dp = [0]*(n+1)

for i in range(1,n+1): 
    time = answer[i][0] - 1
    price = answer[i][1]
    day = time+i
    
    # 상담을 안하는 날이면 기존값과 전날값중 큰것 비교
    dp[i] = max(dp[i-1],dp[i])
    if day<=n:
        dp[day] = max(dp[i-1] + price, dp[day]) # 이전값 가져오기


        
print(dp[n])


