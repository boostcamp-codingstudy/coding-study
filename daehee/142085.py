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
for i, (input_, output) in enumerate(TCs):
    assert solution(*input_) == output, f'The result differs from TC#{i}\ninput:{input_}\noutput:{output}'