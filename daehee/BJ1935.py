A=open(0).read().split()
N,B=int(A[0]),[]
for c in A[1]:
    if 64<ord(c)<91:B+=[int(A[ord(c)-63])]
    else:
        b=B.pop();a=B.pop()
        if c=='*':B+=[a*b]
        elif c=='/':B+=[a/b]
        elif c=='+':B+=[a+b]
        else:B+=[a-b]
print(f'{B[0]:.2f}')