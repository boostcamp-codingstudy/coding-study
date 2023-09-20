from itertools import permutations
n=int(input())
A=list(map(int,input().split()))
oper=list(map(int,input().split()))
op=['+']*oper[0]+['-']*oper[1]+['*']*oper[2]+['/']*oper[3]
answer_max=-1e9
answer_min=1e9
for i in permutations(op,n-1): # 가능한 모든 연산 순서
    total=A[0]
    for j in range(n-1):
        if i[j]=='+':
            total+=A[j+1]
        elif i[j]=='-':
            total-=A[j+1]
        elif i[j]=='*':
            if total<0:
                total=(-total)*A[j+1]*-1
            else:
                total*=A[j+1]
        elif i[j]=='/':
            if total<0:
                total=(-total)//A[j+1]*-1
            else:
                total=total//A[j+1]
    answer_max=max(total,answer_max)
    answer_min=min(total,answer_min)
print(answer_max)
print(answer_min)