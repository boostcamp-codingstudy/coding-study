# https://school.programmers.co.kr/learn/courses/30/lessons/150368
# 코딩테스트 연습 / 2023 KAKAO BLIND RECRUITMENT / 이모티콘 할인행사
# 일일이 케이스

from collections import deque


def solution(users, emoticons):
    answer = []

    ratio = [10, 20, 30, 40]
    cases = deque([[0], [1], [2], [3]])

    for _ in range(len(emoticons)-1):
        temp = []
        while cases:
            case = cases.popleft()
            for i in range(4):
                temp.append(case+[i])

        cases = deque(temp)

    for case in cases:
        plus, extra = 0, 0
        for user in users:
            user_ratio, limit = user
            money = sum(emoticon*(100-ratio[case[i]])//100 for i, emoticon in enumerate(
                emoticons) if ratio[case[i]] >= user_ratio)

            if money >= limit:
                plus += 1
            else:
                extra += money

        answer.append([plus, extra])

    return sorted(answer, key=lambda x: (-x[0], -x[1]))[0]


solution([[40, 10000], [25, 10000]], [7000, 9000])
solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100],
         [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])
