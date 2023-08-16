# https://www.acmicpc.net/problem/1059
# 좋은 구간
# 정렬 및 단순 구현 문제 / 범위 외의 구간을 고려할 것

import sys

L = int(sys.stdin.readline().strip())
S = sorted([0]+list(map(int, sys.stdin.readline().split())))        # 반례 : S의 제일 작은 수보다 앞에 있는 경우 고려
n = int(sys.stdin.readline().strip())

# 이미 S에 n이 있으면 안됨
if n in S:
    print(0)
else:
    result = 0
    for i in range(len(S)-1):
        if S[i]<n<S[i+1]:       # 숫자가 있는 구간 찾기
            max_len = S[i+1]-S[i]-1
            for ml in range(1, max_len):        # 제일 작은 길이부터 확인
                for num in range(S[i]+1, n+1):      # 범위 내에서 길이별 구간을 나누고 n이 있고 범위 안에 있는지 확인해서 구함
                    if num <= n <= num+ml and num+ml < S[i+1]:
                        result += 1
    print(result)    
