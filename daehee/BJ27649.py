# the best solution
s=input()
for e in['<','>','&&','||','(',')']:s=s.replace(e,f' {e} ')
print(' '.join(s.split()))

# the second solution to make it faster but it timed out
# s,a,f=input(),'',0
# for c in s:
#     if f:f=0;continue
#     elif c in ['<','>','(',')']:a+=f' {c} '
#     elif c in ['&','|']:a+=f' {c*2} ';f=1
#     else: a+=c
# print(' '.join(a.split()))