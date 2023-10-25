while True:
    stack=[]
    sentence=input()
    if sentence==".":
        break
    for i in sentence:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(i)
        elif i==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        print("yes")
    else:
        print("no")