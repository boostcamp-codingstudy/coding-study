def p(n):
    for i in range(2,int(n**.5)+1):
        if n%i==0:return False
    return True if n>1 else False
print(sum(p(e)for e in map(int,[*open(0)][1].split())))