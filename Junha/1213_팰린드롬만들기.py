# 규칙대로 문자열 생성
# Reverse 시킨 후에도 같으면 성공

NAME = input()

alpha_dict = dict()

set_name = sorted(list(set(NAME)))

for word in set_name:
    alpha_dict[word] = NAME.count(word)
    
result = ""

middle = ""

if len(NAME) == 1:
    print(NAME)
else:
    if len(set_name) == len(NAME):
        result = sorted(NAME)
    else:
        for i in alpha_dict.keys():
            num = alpha_dict[i]//2
            result += i * num
            alpha_dict[i] -= num

        r_result = "".join(reversed(result))
        for i in r_result:
            alpha_dict[i] -= 1

        for i in alpha_dict.keys():
            if alpha_dict[i] != 0:
                middle = middle + (i * alpha_dict[i])
                alpha_dict[i] -= 1
                
        result = result +  middle + r_result

    reverse_result = "".join(reversed(result))
    if reverse_result == result and sum(alpha_dict.values()) == 0:
        print(result)
    else:
        print("I'm Sorry Hansoo")