def palindrome(num):
    for i in range(len(num)//2):
        if num[i]!=num[len(num)-i-1]:
            return False
    return True
while True:
    num=input()
    if num=='0':
        break
    count=0
    while palindrome(num)==False:
        number=int(num)+1
        count+=1
        num="0"*(len(num)-len(str(number)))+str(number)
    print(count)