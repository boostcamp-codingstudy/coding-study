# https://www.acmicpc.net/problem/1309
# 동물원
# 유사 DP 문제

import sys

N = int(sys.stdin.readline().strip())      # 4

# N=1일때, (0, 0), (0, 1), (1, 0)이 올 수 있으므로 (zero, non_zero) = (1, 2) 이다.
zero_case, non_zero_case = 1, 2
output = zero_case + non_zero_case

# (0, 0)은 모든 경우의 수에서 1번씩 나올 수 있고, (0, 1)의 경우 이전 값이 (0, 1) 또는 (1, 0)인 경우 1번, (0, 0)인 경우 2번씩 나옴
for _ in range(N-1):
    zc, nzc = zero_case, non_zero_case

    zero_case += nzc
    non_zero_case += 2*zc
    output = zero_case + non_zero_case

print(output % 9901)
