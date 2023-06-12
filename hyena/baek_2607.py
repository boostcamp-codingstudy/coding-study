# sys.stdin.readline()
# input()

datas = list([4, 'DOG', 'GOD', 'GOOD', 'DOLL']) # 리스트로 입력

num_range = datas[0]
print(num_range)
base_word = set(datas[1])
print(base_word)
count = 0
for data in datas[2:num_range+1]:
    print(data)
    compare_word = set(data)
    print('compare  ', compare_word)
    if base_word == compare_word: # 두 단어가 같음
        count += 1
        continue
    elif len(base_word) == len(compare_word): # 두 단어의 길이가 같은 경우
        if abs(len(base_word - compare_word)) == 1:
            count += 1
            continue
    else: # 두 단어의 길이가 다른 경우
        if len(compare_word - base_word)==0 and len(base_word - compare_word) <= 1:
            count += 1
            continue
        elif len(base_word - compare_word)==0 and len(compare_word - base_word)<1:
            count += 1
            continue
print(count)  
# return count