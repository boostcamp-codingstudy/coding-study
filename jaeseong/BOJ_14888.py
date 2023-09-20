import sys

sys.stdin = open('input.txt')


n = int(input())

numbers = list(map(int,input().split()))
cal = list(map(int,input().split()))


plus = ["+"]*(cal[0])
minus = ["-"]*(cal[1])
multiple = ["*"]*(cal[2])
divide = ["/"]*(cal[3])

total_cal = plus+minus+multiple+divide

from itertools import permutations

min_value = 1e10 # 조건중요
max_value = -1e10

cal_list = set(permutations(total_cal)) # 중복제거

for i in cal_list:
    value = numbers[0]
    for j in range(len(total_cal)):
        if i[j] == '+': # 연산자가 + 일경우
            value += numbers[j+1] 
        elif i[j] == '-' :
            value -= numbers[j+1] # 빼기
        elif i[j] == '/' and value >=0 : #나누기인데 양수일 경우
            value = value//numbers[j+1]
        elif i[j] == '/' and value <0 : #나누기인데 음수일 경우
            value = -(-value//numbers[j+1])
        else:
            value *= numbers[j+1] 
            
    min_value = min(min_value,value)
    max_value = max(max_value,value)

print(max_value)
print(min_value)
