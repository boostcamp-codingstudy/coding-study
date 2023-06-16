'''
1. 새로운 점수에서 0.5를 뺀 값으로 list에 추가 한다.
2. list를 내림차순 정렬 한다.
3. 등수를 매기면서 추가 했던 새로운 점수를 찾아 등수를 반환 한다.
'''
def solution():
    N, n, P = [int(e) for e in input().split()]
    scores, ranks = [], []
    if N > 0:
        scores = [int(e) for e in input().split()]
    
    scores.append(n - 0.5)
    scores.sort(reverse=True)
    
    rank = 0
    count = 1
    prev = -1
    for i, score in enumerate(scores):
        if score != prev:
            prev = score
            rank += count
            count = 1
        else:
            count += 1
        ranks.append(rank)
        if score == (n - 0.5) and i < P:
            if i == 0:
                return print(ranks[i])
            else:
                if scores[i - 1] == n:
                    return print(ranks[i - 1])
                else:
                    return print(ranks[i])
    print(-1)

solution()