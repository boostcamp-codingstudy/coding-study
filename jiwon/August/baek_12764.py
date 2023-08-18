# https://www.acmicpc.net/problem/12764
# 싸지방에 간 준하

import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())        # 병사 수
cnt = [0]*(N+1)
computer = []
total = 0

people = sorted([list(map(int, sys.stdin.readline().split()))
                 for _ in range(N)], key=lambda x: x[0])
number_ticket = list(range(1, N+1))   # 번호표

for p in people:
    # 다음 병사가 올때까지 사용하는 사람은 모두 내보내기
    while computer and p[0] >= computer[0][0]:
        end, ticket = heappop(computer)
        heappush(number_ticket, ticket)     # 다시 번호표 반납

    # 번호표 뽑고
    seat = heappop(number_ticket)
    heappush(computer, [p[1], seat])

    # 개수 최대값 업데이트
    total = max(total, len(computer))

    # 갯수 저장
    cnt[seat] += 1

# 출력
print(total)
print(*cnt[1:total+1])


'''
    # 우선순위 큐 / deque를 사용, 시간초과 발생 / 리스트를 계속 유지할 필요 없음 => n^2 예상

    import sys
    from heapq import heappush, heappop
    from collections import deque

    N = int(sys.stdin.readline().strip())        # 병사 수

    people = sorted([list(map(int, sys.stdin.readline().split()))
                    for _ in range(N)], key=lambda x: x[0])
    computer = [0]*(N+1)        # 컴퓨터별 사용한 인원 수
    number_ticket = list(range(1, N+1))   # 번호표
    sajibang = []
    time = 0        # 현재 시간

    while people or sajibang:
        if people:
            start, end = people.pop(0)
            time = start        # 현재시간을 시작 시간으로 이동

            # 싸지방에 누가 있는데
            while sajibang:
                # 사용시간을 지나간 병사들만 내보내고 티켓 회수
                if min(sajibang)[0] <= time:
                    _, ticket = heappop(sajibang)
                    computer[ticket] += 1   # 자리 사용한 사람 추가
                    heappush(number_ticket, ticket)
                else:
                    break

            # 번호표 배부
            number = heappop(number_ticket)
            heappush(sajibang, [end, number])  # 이용중인거 표시
        else:
            while sajibang:
                _, ticket = heappop(sajibang)
                computer[ticket] += 1   # 자리 사용한 사람 추가
    result = [c for c in computer[1:] if c != 0]
    print(len(result))
    print(*result)
'''
