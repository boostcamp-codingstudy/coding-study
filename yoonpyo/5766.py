while True:
    n,m=list(map(int,input().split()))
    if n==0 and m==0:
        break
    R={}
    for i in range(n):
        ranking=list(map(int,input().split()))
        for j in ranking:
            if j in R:
                R[j]+=1
            else:
                R[j]=1
    R2=sorted(R.items(),key=lambda x:-x[1])
    answer=[k for k,v in R.items() if v==R2[1][1]]
    answer.sort()
    print(*answer)
    