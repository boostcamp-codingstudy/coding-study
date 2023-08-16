# https://www.acmicpc.net/problem/2090
# 조화 평균
# 유클리드 호제법, gcd 문제

import sys


# 최대 공약수
def gcd(m, n):
    while n:
        m, n = n, m % n
    return m


_ = sys.stdin.readline()
numbers = list(map(int, sys.stdin.readline().split()))

# 분자에 들어갈 모든 숫자의 곱 구하기
numerator = numbers[0]
for n in numbers[1:]:
    numerator *= n

# denominator, numerator = 분모, 분자
denominator = sum([numerator//n for n in numbers])
gcd_number = gcd(numerator, denominator)        # 마지막 분모/분자 의 최대 공약수 계산

print(f"{numerator//gcd_number}/{denominator//gcd_number}")
