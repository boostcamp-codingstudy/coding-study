# https://www.acmicpc.net/problem/1965
# 상자넣기
# 포인트 + dp 방식 / 이전까지 보다 지금이 더 큰지 확인

import sys

N = int(sys.stdin.readline().strip())
_list = list(map(int, sys.stdin.readline().strip().split()))

if len(_list) == 1:
    print(1)
else:
    dp = [1 for _ in range(N+1)]

    for i in range(0, len(_list)):
        for j in range(0, i):
            if _list[j] < _list[i]:         # 지금보다 작은 것을 찾음
                dp[i] = max(dp[i], dp[j]+1)     # 작은것 +1 과 지금을 비교해서 업데이트

    print(max(dp))


'''
    < 메모리 초과 >
    import sys

    N = int(sys.stdin.readline().strip())
    _list = list(map(int, sys.stdin.readline().strip().split()))
    if len(_list) == 1:
        print(1)
    else:
        max_num = max(_list)
        dq = []
        n = _list.pop(0)
        dq.append([n, 1])

        while _list:
            arr = []
            n = _list.pop(0)
            for d in dq:
                if d[0] < n:
                    arr.append([d[0], d[1]])        # 못 넣을 수도 있고
                    arr.append([n, d[1]+1])         # 넣을 수도 있고
                else:
                    arr.append([d[0], d[1]])        # 못 넣는 경우
            dq.extend(arr)

        dq.sort(key=lambda x: x[1], reverse=True)
        print(dq[0][1])
'''
