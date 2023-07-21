import sys

input = sys.stdin.readline
n, k = map(int, input().split())
end = 1
while end < n:
    end *= 2
end = end // 2
print("end", end)
cnt = 0
ans = 0
while True:
    print(n, cnt)
    if cnt > k:
        ans = -1
        break
    if n == 0:
        break
    if n < end:
        end = end // 2
    else:
        n -= end
        cnt += 1
print(ans)
