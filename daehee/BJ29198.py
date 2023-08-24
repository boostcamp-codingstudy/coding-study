*A,=open(0).read().split();n,m,k=map(int,A[:3])
print(''.join(sorted(''.join(sorted(A[3:])[:k]))))