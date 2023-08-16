# https://www.acmicpc.net/problem/12891
# DNA 비밀번호
# sliding window 알고리즘을 활용한 문자열 문제 (시간복잡도 : O(n))

import sys
from collections import deque

S, P = map(int, sys.stdin.readline().split())       # S >= P
dna = sys.stdin.readline().strip()
checked = {k: v for k, v in zip(['A', 'C', 'G', 'T'], list(
    map(int, sys.stdin.readline().split())))}       # DNA 기준점 데이터 추가

dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}      # 문자열에서 확인할 정보
start, end = 0, P-1
dq = deque(dna[start: end])     # 일단 큐에 하나씩 저장
for d in dq:
    dic[d] += 1

result = 0

while end < S:
    # 제일 오른쪽 글자 추가
    dic[dna[end]] += 1

    # 전체 확인
    for k in dic.keys():
        if dic[k] < checked[k]:
            break
    else:
        result += 1

    # 제일 왼쪽 글씨 제거
    dic[dna[start]] = max(0, dic[dna[start]]-1)
    start, end = start+1, end+1     # 다음 턴 준비

print(result)

'''
    # for문이 내부적으로 추가로 돌아 시간초과 발생

    import sys
    from collections import Counter

    S, P = map(int, sys.stdin.readline().split())       # S >= P
    dna = sys.stdin.readline().strip()
    A, C, G, T = map(int, sys.stdin.readline().split())
    idx = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

    result = 0      # 출력

    if S == P:      # 길이가 같으면
        outputs = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for d in dna:
            outputs[d] += 1

        # 하나씩 분석
        for output, check in zip(outputs.values(), [A, C, G, T]):
            if output < check:
                break
        else:
            result += 1
    else:       # S > P (다르면)
        for i in range(S-P+1):
            tokens = [A, C, G, T]
            texts = Counter(dna[i:i+P]).most_common()
            for text in texts:
                tokens[idx[text[0]]] -= text[1]

            if max(tokens) <= 0:
                result += 1

    print(result)
'''
