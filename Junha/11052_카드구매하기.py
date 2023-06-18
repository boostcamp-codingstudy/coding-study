N = int(input())
P = list(map(int,input().split()))

price_per_card = []

for idx,p in enumerate(P):
    price_per_card.append(p/(idx+1))

result = 0

while N:
    high_price_idx = price_per_card.index(max(price_per_card))+1
    if N - high_price_idx >= 0:
        N -= high_price_idx
        result += P[high_price_idx-1]
        print(N,price_per_card)
    else:
        price_per_card[high_price_idx-1] = 0
    

print(result)

# 4개 -> 