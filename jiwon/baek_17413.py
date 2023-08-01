# https://www.acmicpc.net/problem/17413
# 단어 뒤집기 2

import sys
from collections import deque

text = deque(sys.stdin.readline().strip())

result = ""
word = ""
while text:
    t = text.popleft()
    # 공백 문자가 나올때 까지 일단 탐색
    if len(word) > 0 and (t == " " or t == "<"):
        # 공백 문자여도 괄호가 있으면 닫힐때까지는 가지고감
        if word[0] == "<":
            word += t
        else:
            result += word[::-1]+" " if t == " " else word[::-1]
            word = "" if t == " " else "<"
    # 괄호가 닫히면 이전에 열린 괄호가 있다는 얘기니까 그대로 가져가기
    elif t == ">":
        word += t
        result += word
        word = ""
    else:
        word += t

result += word[::-1]        # 마지막 처리

print(result)
