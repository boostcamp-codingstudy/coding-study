# boj 17087 github.com/MuHyeonSon
# # N + D, N - D에서 이동할 수 있는 보폭 D가 고정된 값임을 제대로 이해하지 못해 풀지 못했던 문제
from math import gcd

n, s = map(int, input().split())
location = list(map(int, input().split()))
differences = [abs(s - l) for l in location]
print(gcd(*differences))
