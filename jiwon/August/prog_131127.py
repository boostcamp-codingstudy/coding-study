# https://school.programmers.co.kr/learn/courses/30/lessons/131127
# 코딩테스트 연습 / 연습문제 / 할인 행사
# Counter를 활용한 원소 개수 계산 문제

from collections import Counter


def solution(want, number, discount):
    answer = 0

    # 필요한 품목 리스트 => 딕셔너리
    check_list = {w: n for w, n in zip(want, number)}

    # 순서대로 10개씩 확인
    for i in range(0, len(discount)-9):
        dc_list = Counter(discount[i:i+10]).most_common()
        calc_list = check_list.copy()

        # 품목 리스트에서 원하는 품목이 있으면 뺌
        for dl in dc_list:
            if dl[0] in calc_list.keys():
                calc_list[dl[0]] -= dl[1]

        # 아직도 사야할 품목이 있으면 break, 없으면 answer += 1
        for cl in calc_list.values():
            if cl > 0:
                break
        else:
            answer += 1

    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple",
      "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))    # 3
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana",
      "banana", "banana", "banana", "banana", "banana", "banana"]))     # 0
