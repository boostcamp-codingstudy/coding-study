n,m=map(int,input().split())
package=[]
one=[]
answer=0
for _ in range(m):
    a,b=map(int,input().split())
    package.append(a)
    one.append(b)
package.sort()
one.sort()
while n!=0:
    if n>=6:
        if package[0]>one[0]*6:
            answer+=one[0]*6
        else:
            answer+=package[0]
        n-=6
    else:
        if package[0]<=one[0]*n:
            answer+=package[0]
        else:
            answer+=one[0]*n
        n=0
print(answer)