n=int(input())
map=list(map(str,input()))
cnt=0
for i in range(n):
    if map[i]=='E':
        if map[i-1]=='W':
            cnt+=1
print(cnt)
