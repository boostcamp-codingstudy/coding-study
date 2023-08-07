# https://www.acmicpc.net/problem/1918
# 후위 표기식
# 우선순위를 따지며 스택으로 풀이하는 문제

import sys

formula = sys.stdin.readline().strip()

st, result = [], ""
for f in formula:
    if f.isalpha():     # 문자면 일단 스택에 넣기
       result += f
    else:
        if f == '(':
            st.append(f)
        elif f == '*' or f == '/':
            while st and (st[-1] == '*' or st[-1] =='/'):     # 우선순위가 높은 기호는 모두 추가
                result += st.pop()
            st.append(f)
        elif f == '+' or f == '-':
            while st and st[-1] != '(':     # 우선순위가 높은 기호는 모두 추가
                result+= st.pop()
            st.append(f)
        elif f == ')':
            while st and st[-1] != '(':     # 괄호안에 있는 모든 기호를 표현
                result += st.pop()
            st.pop()

# 남은 기호들 모두 역순으로 넣기
result += ''.join(st[::-1])
    
print(result)