n,m=list(map(int,input().split()))
A=[]
B=[]
for i in range(n):
    A.append(list(map(int,input())))
for i in range(n):
    B.append(list(map(int,input())))
count=0
if n<3 or m<3:
    if A!=B:
        count=-1

for j in range(n-2):
    for k in range(m-2):
        if A[j][k]!=B[j][k]:
            for x in range(j,j+3):
                for y in range(k,k+3):
                    A[x][y]=A[x][y]^1
            count+=1
if A==B:
    print(count)
else:
    print("-1")
