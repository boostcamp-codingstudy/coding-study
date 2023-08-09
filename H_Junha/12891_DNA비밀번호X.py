import sys
import copy
import math

S, P = list(map(int,sys.stdin.readline().split())) #문자열의 길이 S, 비밀번호로 사용한 부분문자열 길이 P
DNA = sys.stdin.readline()
DNA_list = list(map(int,sys.stdin.readline().split()))
DNA_dict = {}
for a,b in zip(DNA_list,"ACGT"):
    DNA_dict[b] = a

gap = S - P

check = {"A" : False,
         "C" : False,
         "G" : False,
         "T" : False}

result = 0
for i in range(gap+1):
    for key, value in DNA_dict.items():
        if DNA[i:i+P].count(key) >= value:
            check[key] = True
            
    if False in check.values():
        pass
    else:
        result += 1
print(result)