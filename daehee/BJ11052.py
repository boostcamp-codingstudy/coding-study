# 정답
'''
card 개수를 순차적으로 늘리면서 card 개수가 늘어날 때 마다 가능한 조합의 비용 중 최대치를 저장 한다. 
(먼저 저장 된 조합의 최대 비용을 참조)
'''
def solution():
    N = int(input())
    prices = [int(e) for e in input().split()]

    costs = [0] * N
    costs[0] = prices[0]
    for i in range(1, N):
        for j in range(i):
            costs[i] = max(costs[i], costs[i - 1 - j] + prices[j], prices[i])

    print(costs[-1])

# 오답
'''
묶음 가격을 평균가 순으로 정렬 하여 평균가가 높은 묶음부터 채워넣는다.
'''
# def solution():
#     N = int(input())
#     prices = [[i + 1, int(e)] for i, e in enumerate(input().split())]
#     prices.sort(key=lambda p : p[1] / p[0], reverse=True)

#     print(prices)
    
#     i = 0
#     cost = 0
#     while N > 0:
#         if N >= prices[i][0]:
#             N -= prices[i][0]
#             cost += prices[i][1]
#         else:
#             i += 1

#     print(cost)

solution()

