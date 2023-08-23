n=int(input())
A=list(map(int,input().split()))

odd=0 #홀수 
even=0 #짝수
for i in range(n):
    if i%2==0:
        odd+=A[i]
    else:
        even+=A[i]
if n==3 and odd>even:
    print(-1)
else:
    print(abs(even-odd))


