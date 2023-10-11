# standard solution using queue
from collections import deque
def solution(x,y,n):
    Q=deque([[x,0]]);A=[];D={}
    while Q:
        x,c=Q.popleft()
        if x==y:A+=[[x,c]]
        p,q,r=x+n,x*2,x*3
        if p<=y and D.get(p,1):Q+=[[p,c+1]];D[p]=0
        if q<=y and D.get(q,1):Q+=[[q,c+1]];D[q]=0
        if r<=y and D.get(r,1):Q+=[[r,c+1]];D[r]=0
    return min(A)[1]if len(A)else -1

# checking answers
TCs =   [
            (
                [10, 40, 5],
                2
            ),
            (
                [10, 40, 30],
                1
            ),
            (
                [2, 5, 4],
                -1
            )
        ]
for i, (input_, output) in enumerate(TCs):
    assert solution(*input_) == output, f'The result differs from TC#{i}\ninput:{input_}\noutput:{output}'