*A,=map(int,open(0).read().split())
n=A[0];A=A[1:]+[0];m,c=0,0
for a in A:
    if a:c+=1
    else:
        if c>m:m=c
        c=0
print(m)