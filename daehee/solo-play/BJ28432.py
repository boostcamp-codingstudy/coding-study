A=open(0).read().split();N=int(A[0])
A,B=A[1:N+1],A[N+2:N+2+int(A[N+1])]
if N==1:exit(print(B[0]))
J=''.join(A);I=J.find('?');f=0
for w in B:
    if I<1:
        if w[-1]==J[I+1]:f=1
    elif len(J)-2<I:
        if w[0]==J[I-1]:f=1
    else:
        if w[0]==J[I-1] and w[-1]==J[I+1]:f=1
    if f and w not in A:print(w)
    f=0