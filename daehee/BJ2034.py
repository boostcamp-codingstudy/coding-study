*A,=map(int,open(0).read().split())
n=A[0];A=A[1:];B=[]
K='AxBCxDxEFxGx'
for i,k in enumerate(K):
    if k=='x':continue
    j,f=i,1
    for a in A:
        j=(j+a)%len(K)
        if K[j]=='x':f=0;break
    if f:print(k,K[j])