n=int(input())
s=list(map(str,input()))
num=[]
stack=[]
for i in range(n):
    num.append(int(input()))
for j in s:
    if j.isalpha()==True: #알파벳이면
        stack.append(num[ord(j)-65])
    else: #연산자면
        str2=stack.pop()
        str1=stack.pop()
        stack.append(eval(str(str1)+j+str(str2)))

print(format(stack[0],".2f"))

