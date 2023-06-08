# https://www.acmicpc.net/problem/2607
# 비슷한 단어
# set, intersection을 활용한 중복 확인

import sys

vocabs = int(sys.stdin.readline().strip())      # 4
first_word = sys.stdin.readline().strip()       # DOG
words = [sys.stdin.readline().strip() for _ in range(vocabs-1)]     # [GOD, GOOD, DOLL]

output = 0      # 출력값
keywords = [tuple(sorted(first_word[:i] + first_word[i+1:])) for i in range(len(first_word))] + [tuple(sorted(first_word))]    # 같거나 하나 추가 된 단어

for word in words:
    tasks = [tuple(sorted(word[:i] + word[i+1:])) for i in range(len(word))] + [tuple(sorted(word))]      # 같거나 하나 뺸 단어

    if set(keywords) & set(tasks):       # list를 set으로 만들려면 tuple로 변경해야 함 (!!!)
        output += 1

print(output)


'''
    <case 2>
    
    import sys

    vocabs = int(sys.stdin.readline())      # 4
    first_word = sys.stdin.readline().strip()   # DOG
    words = [sys.stdin.readline().strip() for _ in range(vocabs-1)]     # [GOD, GOOD, DOLL]

    f = lambda x : [tuple(sorted(x[:i]+x[i+1:])) for i in range(len(x))] + [tuple(sorted(x))]   # lambda 함수화

    output = 0      # 출력값
    keywords = f(first_word)    # 같거나 하나 추가하는 경우

    for word in words:
        tasks = f(word)      # 같거나 하나 빼야하는 경우

        if set(keywords) & set(tasks):       # list를 set으로 만들려면 tuple로 변경해야 함 (!!!)
            output += 1

    print(output)
'''
