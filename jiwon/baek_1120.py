# https://www.acmicpc.net/problem/1120
# 문자열
# 문자열의 길이가 짧아 단순히 인덱싱으로 문자열 비교가 가능

import sys

text1, text2 = sys.stdin.readline().split()

# 1. 같은 길이라면 바로 비교 가능함
if len(text1) == len(text2):
    result = sum([1 for t1, t2 in zip(text1, text2) if t1 != t2])
    print(result)
else:       # len(text1) < len(text2)
    min_num = 50    # text의 최대 길이 = 50
    length = len(text1)
    for i in range(len(text2)-length+1):
        result = sum([1 for t1, t2 in zip(
            text1, text2[i:i+length]) if t1 != t2])
        min_num = min(min_num, result)

    print(min_num)
