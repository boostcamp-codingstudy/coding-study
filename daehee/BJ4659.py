w,v=open(0).read().split(),'aeiou'
b,n,a,f='is','not','acceptable.',1
for W in w[:-1]:
    f,L=1,''
    for i,c in enumerate(W):
        if c in v:L+='0'
        else:L+='1'
    print(f'<{W}>',b,end=' ')
    if'0'not in L:f=0
    elif('000'in L)or('111'in L):f=0
    elif('ee'not in W)and('oo'not in W)and len(W)>1:
        for i in range(len(W)-1):
            if W[i]==W[i+1]:f=0;break
    print(a)if f else print(n,a)