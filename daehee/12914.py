def solution(n):
    a,b=0,1
    for i in range(n):a,b=b,a+b    
    return b%1234567

# checking answers
TCs =   [
            (
                4, 
                5
            ),
            (
                3,
                3
            )
        ]
for i, (input_, output) in enumerate(TCs):
    assert solution(input_) == output, f'The result differs from TC#{i}\ninput:{input_}\noutput:{output}'