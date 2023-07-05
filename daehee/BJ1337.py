A=*map(int,open(0).read().split()),
N,A,M=A[0],sorted(A[1:]),0
for i in range(N):
    C,L=0,[A[i]+j for j in range(1,5)]
    for j in range(i+1,min(i+5,N)):
        if A[j]in L:C+=1
    if C>M:M=C
print(4-M)