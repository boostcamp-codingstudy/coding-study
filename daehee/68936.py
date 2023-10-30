def B(A,n,r,c,Z):
    f,m=0,n//2
    for i in range(r,r+n):
        for j in range(c,c+n):
            if f:=A[r][c]^A[i][j]:
                B(A,m,r,c,Z)
                B(A,m,r,c+m,Z)
                B(A,m,r+m,c,Z)
                B(A,m,r+m,c+m,Z)
                break
        if f:break
    if f==0:Z[A[r][c]]+=1

def solution(A):
    Z=[0,0]
    B(A,len(A),0,0,Z)
    return Z

# checking answers
TCs =   [
            (
                [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]], 
                [4,9]
            ),
            (
                [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]], 
                [10,15]
            )
        ]
for i, (input_, output) in enumerate(TCs):
    assert solution(input_) == output, f'The result differs from TC#{i}\ninput:{input_}\noutput:{output}'