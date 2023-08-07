import sys
from math import ceil
N, M = list(map(int, sys.stdin.readline().split())) #N = 끊어진 기타줄, M = 브랜드 수

n = N
package = []
each = []
for i in range(M):
    p, e = list(map(int, sys.stdin.readline().split()))
    package.append(p)
    each.append(e)

result = 0
while N > 0:
    if N >= 6:
        if min(each) >= min(package)/6:
            result += min(package)
            N -= 6
        else:
            result += min(each)*6
            N -= 6
    else:
        result += min(each)*N
        N -= N

result_1 = min(package)*(ceil(n/6))
result_2 = min(each)*n     

    
print(min([result,result_1,result_2]))
    

    

