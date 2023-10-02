# # standard solution - time limit exceeded
# def solution(N):
#     A=[]
#     for n in N:
#         b=bin(n)[2:];i=1
#         while 1:
#             c=bin(n+i)[2:];d=0
#             for p,q in zip(b.zfill(len(c)),c):d+=(p!=q)
#             if d<3:break
#             i+=1
#         A+=[int(c,2)]
#     return A

# the best solution
solution=lambda N:[((n^(n+1))>>2)+n+1 for n in N]

# checking answers
TCs =   [
            (
                [2, 7], 
                [3,11]
            )
        ]
for i, (input_, output) in enumerate(TCs):
    assert solution(input_) == output, f'The result differs from TC#{i}\ninput:{input_}\noutput:{output}'