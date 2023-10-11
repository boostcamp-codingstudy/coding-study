n,m=map(int,input().split())
A=list(map(int,input().split()))
seat=[]
for i in range(m):
    seat.append(tuple(map(int,input().split())))
seat.sort()
print(seat)

#case1 A=[1,10,100]
# 겹치는 날: 5,6
# 5일 ~ 7일 -> 1 1 1 (100,100,100)
# 2일 ~ 6일 -> 1 1 1 10 10 (100,100,100,10,10)
# 결론: 겹치는 구간 몇 명 몇 일인지 알아내야됨