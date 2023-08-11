# https://www.acmicpc.net/problem/1213
# 팰린드롬 만들기
# dq를 활용한 문제 풀이 / pointer 활용해도 괜찮을 듯

import sys

text = sorted(sys.stdin.readline().strip())      # AABB

output = []
mid = ""

if not text:
    print("I'm Sorry Hansoo")
else:
    while text:
        t1 = text.pop(0)
        if text and text[0] == t1:       # 다음 문자가 같으면 결과에 추가
            text.pop(0)
            output.append(t1)
        elif not mid:           # 하나 단독이면 일단 미드로 저장
            mid = t1
        else:
            output = []
            mid = ""
            break

    if not (output or mid):
        print("I'm Sorry Hansoo")
    else:
        print(f"{''.join(output)}{mid}{''.join(output)[::-1]}")
