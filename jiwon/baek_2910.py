# https://www.acmicpc.net/problem/2910
# 빈도 정렬

import sys
from collections import Counter

N, C = map(int, sys.stdin.readline().strip().split())
_list = Counter(map(int, sys.stdin.readline().strip().split())).most_common()
# Counter.most_common() : (원소, 카운트)의 결과를 출력, 카운트가 같은 요소는 처음 발견된 순서대로 정렬됨
print(' '.join([' '.join([str(x[0])]*x[1]) for x in _list]))
