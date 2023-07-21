a=open(0).read().split()
b,c,d=[0]*25,a[25:],{}
for i in range(25):d[a[i]]=[i//5,i%5]
for k,n in enumerate(c):
    b[5*d[n][0]+d[n][1]]=1
    h=w=0;x=y=1
    for i in range(5):
        t=1
        for j in range(5):t*=b[5*i+j]
        h+=t;x*=b[4*(i+1)];y*=b[6*i]
    for j in range(5):
        t=1
        for i in range(5):t*=b[5*i+j]
        w+=t
    if h+w+x+y>2:print(k+1);break