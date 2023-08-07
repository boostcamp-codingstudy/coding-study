# https://www.acmicpc.net/problem/17413

import sys

sentence = sys.stdin.readline().strip()
# print(sentence)

words = ''
temp = ''
for index, s in enumerate(sentence):
    # print(index, s)
    if s == '<':
        if len(temp) > 0:
            if len(words) > 0 and words[-1] != '>':
                words += ' '
            words += temp
        temp = s
    elif s == '>':
        temp += s
        words += temp
        temp = '' # 문자 비우기
    elif s == ' ':
        if '<' in temp:
            temp += s
        else:
            if len(temp) > 0:
                if len(words) > 0 and words[-1] != '>':
                    words += ' '
                words += temp
                temp = ''
    else:
        if '<' in temp:
            temp += s
            continue
        else:
            temp = s + temp
            if index == len(sentence) -1:
                if len(words) > 0 and words[-1] != '>':
                    words += ' '
                words += temp
    # print('words ', words)
    # print('temp ', temp)

print(words)