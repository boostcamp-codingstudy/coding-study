# standard solution
n,s,_=int(input()),*'* '
e=_*(n-2)
for i in range(2*n-1):
    if i in[0,2*n-2]:print(s*n+2*e+_+s*n)
    elif i==n-1:print(e+_+s+e+s+e+s)
    else:
        a=abs(n-1-i)
        f=_*(n-a-1)
        x=s+e+s
        c=_*(2*a-1)
        print(f+x+c+x)

# # the best solution
# n,a,b=int(input()),*'* '
# m=2*n-3
# s=[a*n+b*m+a*n]
# x=a+b*(n-2)+a
# for i in range(1,n-1):s+=[b*i+x+b*(m-2*i)+x]
# print(*s,b*(n-1)+x+x[1:],*s[::-1],sep='\n')