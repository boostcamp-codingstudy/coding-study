def solution(n,s):
    if s<n:return[-1]
    A=[]
    for i in range(n,0,-1):t=s//i;s-=t;A+=[t]
    return sorted(A)

# checking answers
TCs =   [
            (
                [2, 9], 
                [4, 5]
            ),
            (
                [2, 1], 
                [-1]
            ),
            (
                [2, 8], 
                [4, 4]
            )
        ]
for i, (input_, output) in enumerate(TCs):
    assert solution(*input_) == output, f'The result differs from TC#{i}\ninput:{input_}\noutput:{output}'