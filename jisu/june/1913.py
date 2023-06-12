# 10:25까지
n = int(input())
numlist = [[0 for j in range(n)] for i in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
dd = 1
x = (n - 1) // 2
y = (n - 1) // 2
while cnt <= n * n:
    cnt += 1
    print(x, y)
    numlist[x][y] = cnt
    tmp = 1
    while tmp <= 2:
        x += dx[(tmp - 1) % 4] * dd
        y += dy[(tmp - 1) % 4] * dd
        print(x, y)
        numlist[x][y] = cnt
        tmp += 1
        if cnt > n * n:
            break
    dd += 1
print(numlist)
