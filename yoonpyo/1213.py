from collections import Counter
name=sorted(input())
answer=''
count=0
odd=''
for i in Counter(name).values():
    if i%2==1:
        count+=1
if count>1:
    print("I'm Sorry Hansoo")
else:
    for a,b in Counter(name).items():
        if b%2==0:
            answer+=a*(b//2)
        else:
            if b>2:
                answer+=a*(b//2)
                odd=a
            else:
                odd=a
print(answer+odd+answer[::-1])