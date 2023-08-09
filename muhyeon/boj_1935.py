# boj 1935

# 피연산자의 개수
n = int(input())
# 후위 표기식
post = str(input())
# 피연산자 리스트
numbers = []
# 스택
stack = []

for _ in range(n):
    numbers.append(int(input()))

for c in post:
    if ord(c) >= 65 and ord(c) <= 90:
      stack.append(numbers[ord(c) - 65])
      continue
    number2 = stack.pop()
    number1 = stack.pop()
    stack.append(eval(str(number1) + str((c) + str(number2))))

print(f'{stack[0]:.2f}')
