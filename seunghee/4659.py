import sys
from collections import Counter
while True:
    password = str(sys.stdin.readline().strip())
    if password == 'end':
        break
    
    transform_num = list('3'*len(password))
    for i, word in enumerate(list(password)):
        if 'a' in word or 'i' in word or 'u' in word:
            transform_num[i] = '0'
        elif 'e' in word or 'o' in word:
            transform_num[i] = '1'
    print(password, transform_num)
    # if not ('a' in password or 'e' in password or 'i' in password or 'o' in password or 'u' in password):
    #     print(f'<{password}> is acceptable.')
    #     continue
        
    # if 





