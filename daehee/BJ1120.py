a,b=input().split()
l,m,d,t=len(a),len(b),0,50
if l==m:
    for i in range(l):
        if a[i]!=b[i]:d+=1
    print(d)
else:
    for i in range(m-l+1):
        c,d=b[0:i]+a+b[i+l:],0
        for i in range(m):
            if c[i]!=b[i]:d+=1
        if d<t:t=d
    print(t)