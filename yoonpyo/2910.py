from collections import Counter
n,c=list(map(int,input().split()))
message=list(map(int,input().split()))
answer=[]
m=Counter(message).most_common()
for k,v in m:
    #그냥 Counter와 elements는 items()했을 때 순서 유지가 안됨
    for i in range(v):
        answer.append(k)
print(*answer)