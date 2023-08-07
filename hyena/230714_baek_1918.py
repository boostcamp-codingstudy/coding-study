# https://www.acmicpc.net/problem/1918
# done

# G*(A-B*(C/D+E)/F) -> GABCD/E+*F/-*
# A*B*C -> AB*C*
# A*(B+C)/D -> ABC+*D/
# A+(B-C)/D -> ABC-D/+
# A+B*C+D -> ABC*+D+

# A+B+C+D -> AB+C+D+
# A+B*C+D*E+G -> ABC*+DE*+G+
# A*B+C+D+E*F*G+E -> AB*C+D+EF*G*+E+

import sys

exp = sys.stdin.readline().strip()

operator = [] # 연산자만 관리
result = ''

for index, e in enumerate(exp):
    # print('operator ', operator, len(operator))
    # print('result ', result, len(result))
    # print(e)

    # operand
    if e not in '+-*/()':
        result += e
        continue
    # bracket
    if e in '(':
        operator.append(e)
        continue
    elif e in ')':
        while True:
            if operator[-1] == '(':
                operator.pop()
                break
            result += operator.pop()
    # operator
    if e in '*/':
        if len(operator) != 0 and operator[-1] in '*/': # G*(A-B*(C/D+E)/F) -> GABCD/E+*F/-*
            result += operator.pop()
        operator.append(e)
        continue
    elif e in '+-':
        if len(operator) != 0 and operator[-1] in '*/':
            for _ in range(len(operator)):
                if operator[-1] == '(':
                    break
                result += operator.pop()
        if len(operator) != 0 and operator[-1] in '+-': # A+B+C+D -> AB+C+D+
            result += operator.pop()
        operator.append(e)

# print(operator, len(operator))
# print(result, len(result))
for _ in range(len(operator)):
    result += operator.pop()
    
print(result)
