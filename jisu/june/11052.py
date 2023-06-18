# 23. 06. 16
n = int(input())
lst = list(map(int, input().split()))
for i in range(1, n + 1):
    cmp = []
    if i == 1:
        continue
    start = i - 1
    dell = i - start
    for j in range(i // 2):
        lst[i - 1] = max(lst[i - 1], lst[start - 1] + lst[dell - 1])
        start -= 1
        dell += 1
print(lst[n - 1])
