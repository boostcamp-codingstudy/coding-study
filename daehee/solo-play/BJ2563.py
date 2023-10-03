*A,=map(int,open(0).read().split())
n=A[0];A=A[1:];B=[0]*10000
for i in range(n):
    y,x=A[2*i:2*i+2]
    for r in range(10):
        for c in range(10):B[100*(r+y)+c+x]=1
print(sum(B))