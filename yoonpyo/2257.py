chemical=list(input())
stack=[]
answer=0
for i in chemical:
    if i=='(':
        stack.append(answer)
        answer=0
        stack.append(i)
    elif i==')':
        num=0
        while True:
            a=stack.pop()
            if a=='(': # '('가 나올때까지 pop
                break
            num+=a # 괄호 사이의  수 계속 더하기
        stack.append(num)
    elif i=='H':
        stack.append(1)
    elif i=='C':
        stack.append(12)
    elif i=='O':
        stack.append(16)
    else:
        a=stack.pop()
        stack.append(a*int(i))
print(sum(stack))