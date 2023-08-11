# https://school.programmers.co.kr/learn/courses/30/lessons/150367
# 표현 가능한 이진트리
# 포화 이진트리의 구조를 이해해야 하는 내용

import sys


def search(number):     # 완전 이진 트리임을 탐색
    length = len(number)
    if length == 1 or '1' not in number or '0' not in number:
        return True

    mid = length // 2
    if number[mid] == '0':
        return False

    return search(number[:mid]) and search(number[mid+1:])


def solution(numbers):
    answer = []
    binary_nums = [2**i - 1 for i in range(50)]      # 이진트리 생성

    for number in numbers:
        number = bin(number)[2:]
        length = len(number)
        for bn in binary_nums:      # 포화 이진트리 맞춰주기
            if bn >= length:
                number = number.rjust(bn, '0')
                break
        answer.append(1 if search(number) else 0)
    return answer


if __name__ == "__main__":
    print(solution(list(map(int, sys.stdin.readline().split()))))
