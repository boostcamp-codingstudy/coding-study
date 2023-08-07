a=open(0).read().split()
n,m,w,d,s,h=int(a[0]),int(a[1]),a[2:],'ACGT','',0
for j in range(m):
    c=[0]*4
    for i in range(n):
        c[d.index(w[i][j])]+=1
    s+=d[c.index(max(c))]
for j in range(m):
    for i in range(n):
        h+=(s[j]!=w[i][j])
print(s)
print(h)