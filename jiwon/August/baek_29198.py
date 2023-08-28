# https://www.acmicpc.net/problem/29198
# 이번에는 C번이 문자열
# sorting + 그리디 알고리즘 문제, 문자열을 계속 정렬하면서 사전순에 맞는 단어를 찾는 것이 목적

import sys


N, M, K = map(int, sys.stdin.readline().split())
texts = sorted([''.join(sorted(sys.stdin.readline().strip()))
               for _ in range(N)])
result = ''.join(sorted(''.join(texts[:K])))
print(result)
