def solution(places):
    A=[1]*5;D=[[r,c]for r in range(3)for c in range(-2,3)if abs(r)+abs(c)<3 and(r or c)]
    for k,P in enumerate(places):
        M=[[0]*5 for _ in range(5)];f=0
        for i in range(5):
            for j in range(5):
                if P[i][j]=='P'and M[i][j]==0:
                    M[i][j]=1
                    for d in D:
                        u,v=i+d[0],j+d[1]
                        if u<0 or u>4 or v<0 or v>4:continue
                        if P[u][v]=='P':
                            m=abs(d[0])+abs(d[1])
                            if m==1:f=1;break
                            elif m==2:
                                if d[0]==2 and P[i+1][j]=='O':f=1;break
                                elif d[1]==2 and P[i][j+1]=='O':f=1;break
                                elif d==[1,1]:
                                    if P[i][j+1]=='O' or P[i+1][j]=='O':f=1;break
                                elif d==[1,-1]:
                                    if P[i][j-1]=='O' or P[i+1][j]=='O':f=1;break
                if f:break               
            if f:break
        if f:A[k]=0
    return A

# checking answers
TCs =   [
            (
                [
                    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
                    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
                    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
                    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
                    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
                ], 
                [
                    1, 
                    0, 
                    1, 
                    1, 
                    1
                ]
            )
        ]
for i, (input_, output) in enumerate(TCs):
    assert solution(input_) == output, f'The result differs from TC#{i}\ninput:{input_}\noutput:{output}'