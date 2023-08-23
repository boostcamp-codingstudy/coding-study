# boj 1448 삼각형 만들기
import sys

n = int(input())
length = sorted([int(sys.stdin.readline().strip()) for i in range(n)], reverse=True)
result = -1

for i in range(n-2):
    if length[i] < length[i+1] + length[i+2]:
        print(length[i+1] + length[i+2] + length[i])
        exit()

print(result)

# 1448번. 삼각형 만들기

'''
import sys
input = sys.stdin.readline

n = int(input())
nList = []
for i in range(n):
    nList.append(int(input()))

nList.sort(reverse=True)

for i in range(n-2):
    if nList[i] < nList[i+1] + nList[i+2]:
        print(nList[i] + nList[i+1] + nList[i+2])
        exit()
print(-1)
# => 이거는 가장 큰수와 나란히 있는 숫자들의 경우밖에 고려 못하는 거 아닌지,, 왜 답일까
# Reference : https://chance0523.github.io/algorithm/2021/09/26/algorithm-%EC%82%BC%EA%B0%81%ED%98%95%EB%A7%8C%EB%93%A4%EA%B8%B0/
'''


''' 시간초과
import sys

n = int(input())
length = sorted([sys.stdin.readline().strip() for i in range(n)], reverse=True)
print(length)
def maximum_three_side(n):
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if length[j] + length[k] > length[i]:
                    return  length[j] + length[k] + length[i]

print(maximum_three_side(n))    
'''
''' 시간초과  발생
from itertools import combinations # 실버 난이도 이하에서는 itertools x

n = int(input())
length = []
for _ in range(n):
    length.append(int(input()))

combination_triangle = list(combinations(length, 3))

result = -1

for candidate in combination_triangle:
    list(candidate).sort()
    if  sum(candidate[:-1]) > candidate[-1]: ## 
        result = max(result, sum(candidate))

print(result)
'''


'''
세준이는 N개의 빨대를 가지고 있다. N개의 빨대 중에 3개의 빨대를 선택했을 때, 이 빨대로 삼각형을 만들 수 있다면, 세 변의 길이의 합의 최댓값을 구하고 싶다.

입력
첫째 줄에 빨대의 개수 N이 주어진다. N은 3보다 크거나 같고, 1,000,000보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 빨대의 길이가 한 줄에 하나씩 주어진다.
 빨대의 길이는 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 삼각형 세 변의 길이의 합의 최댓값을 출력한다. 만약 삼각형을 만들 수 없으면 -1을 출력한다.

예제 입력 1 
3
1
2
3
예제 출력 1 
-1
예제 입력 2 
3
1
2
2
예제 출력 2 
5
예제 입력 3 
6
2
3
2
3
2
4
예제 출력 3 
10
예제 입력 4 
5
4
5
6
7
20
예제 출력 4 
18
'''
