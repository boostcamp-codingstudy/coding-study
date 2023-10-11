n,m=map(int,input().split())
square=[]
for i in range(n):
    square.append(list(map(int,input().split())))
fb=0
lr=0
for i in range(n):
    for j in range(m-1):
        if square[i][j]>square[i][j+1]:
            lr+=square[i][j]-square[i][j+1]
    lr+=square[i][m-1]

for i in range(m):
    for j in range(n-1):
        if square[j][i]>square[j+1][i]:
            fb+=square[j][i]-square[j+1][i]
    fb+=square[n-1][i]
print(2*(lr+fb+n*m))
#     2 3 5
# 4 <-1 3 4-> 4
# 3 <-2 2 3 -> 3
# 4 <-1 2 4 -> 4
#     2 3 5
# 아래, 위: nxm