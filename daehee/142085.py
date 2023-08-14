import heapq as hq

def solution(n, k, enemy):
    heapEnemy = []
    for round in range(len(enemy)):
        hq.heappush(heapEnemy, enemy[round])
        if len(heapEnemy) > k:
            n -= hq.heappop(heapEnemy);
        if n < 0:
            return round;
    return len(enemy)


# checking answers
TCs = [
    ((7, 3, [4, 2, 4, 5, 3, 3, 1]), (5)), 
    ((2, 4, [3, 3, 3, 3]), (4))
]
for i, (input, output) in enumerate(TCs):
    assert solution(*input) == output, f'TC#{i}incorrect\ninput:{input}\noutput:{output}'