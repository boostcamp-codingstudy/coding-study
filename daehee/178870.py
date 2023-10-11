# # standard solution - time limit exceeded
# def solution(A,k):
#     n=len(A);R=[]
#     for i in range(n):
#         s,j=0,i
#         while (s<k)&(j<n):s+=A[j];j+=1
#         if s==k:R+=[[i,j-1]]
#     return sorted(R,key=lambda e:[e[1]-e[0],e[0]])[0]

# standard solution using two-pointer
def solution(A,k):
    A+=[0];n=len(A);R=[];s,i,j=0,0,0
    while (i<n)&(j<n):
        if s<k:s+=A[j];j+=1
        elif s>k:s-=A[i];i+=1
        else:R+=[[i,j-1]];s-=A[i];i+=1
    return sorted(R,key=lambda e:[e[1]-e[0],e[0]])[0]

# checking answers
TCs =   [
            (
                [[1, 2, 3, 4, 5], 7],
                [2, 3]
            ),
            (
                [[1, 1, 1, 2, 3, 4, 5], 5],
                [6, 6]
            ),
            (
                [[2, 2, 2, 2, 2], 6],
                [0, 2]
            )
        ]
for i, (input_, output) in enumerate(TCs):
    assert solution(*input_) == output, f'The result differs from TC#{i}\ninput:{input_}\noutput:{output}'