# https://www.acmicpc.net/problem/1969
# done

import sys

num, chr_num = map(int, sys.stdin.readline().split())

words = []
for _ in range(num):
    word = sys.stdin.readline().strip('\n')
    words.append(word)

# print(words)
result_str = ''
result_count = 0
for i in range(chr_num):
    count = {}
    for word in words:
        if word[i] not in count:
            count[word[i]] = 0
        count[word[i]] += 1
    # print(i, count)
    count = dict(sorted(count.items(), key = lambda x:x[0]))
    # print(max(count, key = count.get))
    max_key = max(count, key = count.get)
    result_str += max_key
    result_count += (num - count[max_key])

print(result_str)
print(result_count)
