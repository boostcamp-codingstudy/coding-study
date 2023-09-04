*A,=map(int,open(0).read().split())
s=A[-1]
for a in A[1:][::-1]:
    if s%a:
        if a>s:s=a
        else:s=a*(s//a+1)
print(s)