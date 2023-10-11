def solution(N):
    S = list(map(str,N))
    S.sort(key=lambda x:x*3)
    return str(int(''.join(S[::-1])))

# checking answers
TCs =   [
            (
                [6, 10, 2], 
                "6210"
            ),
            (
                [3, 30, 34, 5, 9],
                "9534330"
            )
        ]
for i, (input_, output) in enumerate(TCs):
    assert solution(input_) == output, f'The result differs from TC#{i}\ninput:{input_}\noutput:{output}'