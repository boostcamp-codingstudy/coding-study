'''
입력 받은 문자열을 순차 탐색 한다.
괄호가 열릴 때, stack에 0을 추가 한다.
문자가 들어올 때, 해당 하는 숫자를 추가 한다.
숫자가 들어올 때, 직전의 숫자에 곱하고 저장 한다.
괄호가 닫힐 때, 최근 0 전까지 수들을 더하고 저장 한다.
'''
def solution():
    formula = input()
    elements = {'H' : 1, 'C' : 12, 'O' : 16}
    stack = [0]
    for c in formula:
        if c == '(':
            stack.append(0)
        elif c == ')':
            temp_sum = 0
            while stack[-1] > 0:
                temp_sum += stack.pop(-1)
            stack[-1] += temp_sum
        elif c in '23456789':
            stack[-1] *= int(c)
        else:
            stack.append(elements[c])
    print(sum(stack))

solution()