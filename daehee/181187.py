# # standard solution - time limit exceeded
# def solution(a,b):
#     s,l,c=a*a,b*b,0
#     for x in range(b+1):
#         t=x*x
#         for y in range(b+1):
#             t+=y*y
#             if s<=t<=l:c+=1
#     return c

# standard solution 2 using math
from math import sqrt, ceil, floor
def solution(a,b):
    s,l,c=a*a,b*b,0
    for x in range(1,b+1):
        t=x*x
        i=0 if x>a else ceil(sqrt(s-t))
        j=floor(sqrt(l-t))
        c+=(j-i+1)
    return 4*c

# standard solution 3
# from math import sqrt
# def solution(a,b):
#     s,l,c=a*a,b*b,0
#     for x in range(b):
#         t=x*x;
#         c+=int(sqrt(l-t))-(0 if x>=a else int(sqrt(s-t-1)))
#     return 4*c

# checking answers
TCs =   [
            (
                [2, 3], 
                20
            )
        ]
for i, (input_, output) in enumerate(TCs):
    assert solution(*input_) == output, f'The result differs from TC#{i}\ninput:{input_}\noutput:{output}'