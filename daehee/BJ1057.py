n,a,b=map(int,open(0).read().split());i=0;a-=1;b-=1
while abs(a-b):a//=2;b//=2;i+=1
print(i)