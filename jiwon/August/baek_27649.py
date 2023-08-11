# https://www.acmicpc.net/problem/27649
# 토크나이저
# 문자열 replace + split/join

import sys

text = sys.stdin.readline().strip()
operation = ["<", ">", "(", ")", "||", "&&"]
for op in operation:
    text = text.replace(op, f" {op} ")

print(' '.join(text.split()))


'''
    # 일일이 하나씩 시도했다가 시간초과가 남
    # 공백이 여러개 있는것은 split으로 제거할 수 있으니 해당 문자를 replace 하는 것으로 접근

    import sys

    text = ' '.join(sys.stdin.readline().split())
    i = 0

    text = text.replace("||", "|").replace("&&", "&")

    while i < len(text):
        if text[i] in ["<", ">", "(", ")", "|", "&"]:
            try:
                if text[i-1] != " ":
                    text = text[:i] + " " + text[i:]
                    i += 1
            except IndexError:
                pass
            try:
                if text[i+1] != " ":
                    text = text[:i+1] + " " + text[i+1:]
            except IndexError:
                pass

        i += 1

    text = text.replace("|", "||").replace("&", "&&")

    print(text)

'''
