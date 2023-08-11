# https://www.acmicpc.net/problem/17087
# 숨바꼭질 6
# 최대공약수 문제
  
import sys

N, S = map(int, sys.stdin.readline().split())
sisters = sorted(map(int, sys.stdin.readline().split()))
distance = [abs(s-S) for s in sisters]

# 유클리드 호제법을 활용한 최대공약수
def gcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n

# 여러수의 최대공약수를 구할때는 하나씩 구해나가면 됨
result = distance[0]
for d in distance[1:]:
    result = gcd(result, d)
    
print(result)