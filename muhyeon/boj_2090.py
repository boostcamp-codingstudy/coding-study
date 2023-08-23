# boj 2090 조화평균

from math import lcm, gcd

n = int(input())
a = list(map(int, input().split()))

lcm_a = lcm(*a)
denominators = lcm_a # 분모
numerators = 0 # 분자
for i in a:
    numerators += lcm_a // i

gcd_a = gcd(denominators, numerators)
print(f'{denominators // gcd_a}/{numerators // gcd_a}')
