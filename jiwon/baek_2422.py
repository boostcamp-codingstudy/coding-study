# https://www.acmicpc.net/problem/2422
# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# 표를 작성하여 문제를 해결하는 브루트포스 문제

import sys
from itertools import combinations as cbs

N, M = map(int, sys.stdin.readline().strip().split())         # 5 3
_input = [sys.stdin.readline().strip()
          for _ in range(M)]       # 1 2 / 3 4 / 1 3
bad_choices = [list(map(int, x.split())) for x in _input]
tasks = map(set, cbs(range(1, N+1), 3))

dp = [[1]*(N+1) for _ in range(N+1)]        # 표를 작성
for bc in bad_choices:
    dp[bc[0]][bc[1]] = 0
    dp[bc[1]][bc[0]] = 0

result = 0
for task in tasks:
    n1, n2, n3 = task
    if dp[n1][n2] and dp[n2][n3] and dp[n1][n3]:        # 하나라도 있으면 아웃
        result += 1

print(result)

'''
    import sys
    from itertools import combinations as cbs

    N, M = map(int, sys.stdin.readline().strip().split())         # 5 3
    _input = [sys.stdin.readline().strip()
            for _ in range(M)]       # 1 2 / 3 4 / 1 3
    bad_choices = [list(map(int, x.split())) for x in _input]

    tasks = map(set, cbs(range(1, N+1), 3))
    output = 0
    for task in tasks:
        for bc in bad_choices:
            if len(task-set(bc)) == 1:      # 원래는 set을 사용하여 중복되는 것들을 제거 했는데 시간초과남
                break
        else:
            output += 1

    print(output)
'''
