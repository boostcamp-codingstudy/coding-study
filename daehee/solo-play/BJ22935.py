a=*map(int,open(0).read().split()),
for i in range(a[0]):
    n=a[i+1]-1;q,r=n//14,n%14
    if q%2:s=bin(15-r)
    else:s=bin(r+1)
    print(s[2:].zfill(4).replace('0','V').replace('1','딸기'))