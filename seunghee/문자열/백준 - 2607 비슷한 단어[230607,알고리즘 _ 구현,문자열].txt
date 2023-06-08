# N = int(input())
# word = list(str(input()))
# data = [map(str, input()) for _ in range(N-1)]
N = 4
word = list('DOG')
data = ['GOD', 'GOOD', 'DOLL']
answer =0 

for compare in data:
    first_word = word[:]
    count = 0 # 한 단어씩 비교
    for char in compare:
        if char in first_word:
            first_word.remove(char)
        else:
            count += 1 # 비교단어 중에서 첫번째랑 비교할때 없는 것

    if count <= 1 and len(first_word) <= 1: # 차이가 하나 이하면 되는건가?
        # len(first_word) 첫번째 단어중에서 비교단어와 비교할때 없는 것
        answer += 1
print(answer)