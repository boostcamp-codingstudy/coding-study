def solution(W, N, D):
    a,b,c={},{},0
    for w,n in zip(W,N):a[w]=n
    for i in range(10):
        d=D[i]
        if b.get(d,0):b[d]+=1
        else:b[d]=1
    for i in range(-1,len(D)-10):
        if i>=0:
            b[D[i]]-=1;d=D[i+10]
            if b.get(d,0):b[d]+=1
            else:b[d]=1
        f=1
        for e in a:
            if a[e]>b.get(e,0):f=0;break
        c+=f
    return c


# checking answers
TCs = [
    ((["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]), (3)), 
    ((["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]), (0))
]
for i, (input_, output) in enumerate(TCs):
    assert solution(*input_) == output, f'The result differs from TC#{i}\ninput:{input_}\noutput:{output}'