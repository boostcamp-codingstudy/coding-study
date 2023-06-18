# https://www.acmicpc.net/problem/2257
# 화학식량
# stack을 활용한 계산 문제

import sys

hhs = sys.stdin.readline().strip()      # (H)2(O)
const = {"C": 12, "H": 1, "O": 16}

stack = []
for h in hhs:
    if h == '(':            # (
        stack.append(h)
    elif h.isalpha():       # C, H, O
        stack.append(const[h])
    elif h.isdigit():       # 2, 3, 4, 5, 6, 7, 8, 9
        stack.append(stack.pop() * int(h))
    else:                   # )
        dq = []
        while stack:
            if stack[-1] == "(":
                stack.pop()
                break
            dq.append(stack.pop())

        stack.append(sum(dq))

print(sum(stack))
