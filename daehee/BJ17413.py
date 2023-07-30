# # standard solution
# S,f='',0
# for c in input():
#     if c=='<':f=1;print(S[::-1],end='');S=c
#     elif c=='>':f=0;print(S+c,end='');S=''
#     elif c==' 'and f!=1:print(S[::-1],end=' ');S=''
#     else:S+=c
# if S:print(S[::-1])

# the best solution
s=input().replace('>','<').split('<')
print(''.join(f'<{s[i]}>'if i%2 else' '.join(e[::-1]for e in s[i].split())for i in range(len(s))))