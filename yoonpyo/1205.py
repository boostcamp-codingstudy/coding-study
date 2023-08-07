n,score,p=list(map(int,input().split()))
rank=n+1 #rank가 계속 안바뀌면 맨 마지막 rank
if n>0: #n이 0보다 클때 
    rankinglist=list(map(int,input().split()))
    rankinglist.sort(reverse=True) #내림차순 정렬
    print(rankinglist)
    if n==p and score<=rankinglist[-1]:
        #올라갈 수 있는 점수 개수와 리스트 숫자 개수가 같고, 가장 작은 수가 score보다 크거나 같으면 
        print(-1)
    else:
        for i in range(n):
            if score>=rankinglist[i]: #score가 rankinglist의 숫자보다 크거나 같을때  # 10 9 8 7 6 ~~~
                rank=i+1
                break
        print(rank)
else: #n=0일때 무조건 1
    print(1)