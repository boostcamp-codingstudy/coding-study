# standard solution using brute force
O=['','I','II','III','IV','V','VI','VII','VIII','IX']
T=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
B='IVXLC';D={}
for i in range(1,100):
    A=T[i//10]+O[i%10];C=[0]*5
    for a in A:C[B.index(a)]+=1
    b=''.join(map(str,C))
    if D.get(b,0):D[b]+=[A]
    else:D[b]=[A]
A=input();C=[0]*5
for a in A:C[B.index(a)]+=1
print(D[''.join(map(str,C))][0])