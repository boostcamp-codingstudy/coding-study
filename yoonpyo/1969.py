n,m=list(map(int,input().split()))
dna=[]
answer=''
hamming=0
for i in range(n):
    dna.append(list(input()))
for i in range(m):
    t=a=g=c=0
    for j in range(n):
        if dna[j][i]=='T':
            t+=1
        elif dna[j][i]=='A':
            a+=1
        elif dna[j][i]=='G':
            g+=1
        elif dna[j][i]=='C':
            c+=1
    hamming+=(n-max(t,a,g,c))
    if max(t,a,g,c)==a:
        answer+='A'
    elif max(t,a,g,c)==c:
        answer+='C'
    elif max(t,a,g,c)==g:
        answer+='G'
    elif max(t,a,g,c)==t:
        answer+='T'
print(answer)
print(hamming)
        
            