n = int(input())
word = list(input())
answer = 0

for _ in range(N-1):
    compare = word[:] 
    word2 = input() 
    count = 0

    for w in word2:
        if w in compare:
            compare.remove(w)
        else:
            count += 1

    if count <=1 and len(compare) <=1:
        answer += 1

print(answer)