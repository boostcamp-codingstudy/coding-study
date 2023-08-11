# https://www.acmicpc.net/problem/1935
# 후위 표기식 2
# 스택을 활용한 후위식 문제풀이

import sys

N = int(sys.stdin.readline().strip())
lines = sys.stdin.readline().strip()

numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]

stack = []
num_dict = {}
for l in lines:
    if l.isalpha():
        # 이미 해당 문자에 숫자가 할당되었으면 패스, 아니면 추가
        if l not in num_dict.keys():        
            num_dict[l] = numbers.pop(0)
        num = num_dict[l]
        stack.append(num)
    else:
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(eval(f"{n2}{l}{n1}"))
    
print("{:.2f}".format(stack[-1]))