import sys

input = sys.stdin.readline
n, m = map(int, input().split())
origin = [list(input().rstrip()) for j in range(n)]
change = [list(input().rstrip()) for j in range(n)]
same = 0
if origin == change:
    same = 1
for i in range(n):
    for j in range(m):
        if origin[i][j] == "0":
            origin[i][j] = -1
        else:
            origin[i][j] = 1
        if change[i][j] == "0":
            change[i][j] = -1
        else:
            change[i][j] = 1
ccnt = 0
for i in range(n - 2):
    for j in range(m - 2):
        if origin[i][j] != change[i][j]:
            ccnt += 1
            origin[i][j] *= -1
            origin[i + 1][j] *= -1
            origin[i + 2][j] *= -1
            origin[i][j + 1] *= -1
            origin[i + 1][j + 1] *= -1
            origin[i + 2][j + 1] *= -1
            origin[i][j + 2] *= -1
            origin[i + 1][j + 2] *= -1
            origin[i + 2][j + 2] *= -1
if origin != change:
    print("-1")
else:
    if (n < 3) or (m < 3):
        if same == 1:
            print("0")
        else:
            print("-1")
    else:
        print(ccnt)
