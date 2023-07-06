while True:
    password=input()
    count=0
    count2=0
    vowels={'a','e','i','o','u'}
    if password=="end":
        break
    #조건1
    if 'a' in password or 'e' in password or 'i' in password or 'o' in password or 'u' in password:
        count+=1
    #조건3
    if len(password)>=2:
        for i in range(len(password)-1):
            if password[i]==password[i+1] and (password[i]!='e' and password[i]!='o'):
                    count2+=1
    #조건2
    if len(password)>=3:
        for i in range(len(password)-2):
            if password[i] in vowels and password[i+1] in vowels and password[i+2] in vowels:
                count2+=1
            elif password[i] not in vowels and password[i+1] not in vowels and password[i+2] not in vowels:
                count2+=1
    if count==1 and count2==0:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
    
    