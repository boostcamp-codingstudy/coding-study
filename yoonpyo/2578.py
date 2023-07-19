bingo=[[0]*5 for _ in range(5)]
answer=[]
for i in range(5):
    bingo[i]=list(map(int,input().split()))
for i in range(5):
    answer+=list(map(int,input().split()))

def countbingo():
    answer=0
    for i in range(5):
        if bingo[i].count(0)==5:
            answer+=1

    for i in range(5):
        count=0 # 세로
        for j in range(5):
            if bingo[j][i]==0:
                count+=1
        if count==5:
            answer+=1

    count2=0 #왼쪽 대각선
    count3=0 # 오른쪽 대각선
    for i in range(5):
        if bingo[i][i]==0:
            count2+=1
        if bingo[i][4-i]==0:
            count3+=1
    if count2==5:
        answer+=1
    if count3==5:
        answer+=1

    return answer
        

for t in range(25):
    for x in range(5):
        for y in range(5):
            if bingo[x][y]==answer[t]:
                bingo[x][y]=0
    num=countbingo()
    if num>=3: # num==3
        print(t+1)
        break