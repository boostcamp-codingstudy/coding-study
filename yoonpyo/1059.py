l=int(input())
nlist=list(map(int,input().split()))
n=int(input())
answer=0
nlist.sort()
if nlist[0]>n:
    answer=((nlist[0]-n)*n)-1 # 가장 작은 숫자보다도 작을 때
for i in range(1,l):
    if nlist[i-1]<n and nlist[i]>n:
        answer=(nlist[i]-n)*(n-nlist[i-1])-1

print(answer)
        
            
# 2 (3,4,5,6) -> 1*4 - 0
# 9 (10, 11, 12), 10 (11, 12) -> 2*3 - 1 (10,10인 경우)
# 34 (59~99), 35 (59~99), ....59 (60~99)
# 34~59=26, 59~99=41 -> 26*41=1066 - 1

# 시작점: (리스트값~n) ~(n~리스트다음값) 
# 반례: nlist=(7,8,9) n=2 -> 9