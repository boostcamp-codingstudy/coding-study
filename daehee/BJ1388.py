# standard solution
*A,=open(0).read().split()
n,m=map(int,A[:2]);A=A[2:];c=0
for i in range(n):
    for j in range(m):
        if A[i][j]=='-':
            if j:c+=A[i][j-1]!=A[i][j]
            else:c+=A[i][j]=='-'
        else:
            if i:c+=A[i-1][j]!=A[i][j]
            else:c+=A[i][j]=='|'
print(c)