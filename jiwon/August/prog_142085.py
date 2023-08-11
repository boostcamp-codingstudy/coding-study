# https://school.programmers.co.kr/learn/courses/30/lessons/142085
# 코딩테스트 연습 / 연습문제 / 디펜스 게임
# 우선순위 큐 문제 / heapq로 순서 지속적으로 유지

from heapq import heappush, heappop


def solution(n, k, enemy):
    answer = 0
    limit = 0

    hp = []

    for e in enemy:
        heappush(hp, -e)
        limit += e

        # 적의 수를 다 더하고
        if limit > n:
            # 무적권이 없으면 끝
            if k == 0:
                return answer
            limit += heappop(hp)
            k -= 1

        answer += 1

    return answer


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
print(solution(2, 4, [3, 3, 3, 3]))
