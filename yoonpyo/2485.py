from math import gcd
import sys
n=int(sys.stdin.readline())
arr1=[]
arr2=[]
for i in range(n):
    arr1.append(int(sys.stdin.readline()))
for i in range(1,n):
    arr2.append(arr1[i]-arr1[i-1])
s=arr2[0]
for j in range(1,n-1):
    s=gcd(s,arr2[j])
count=0
start=arr1[0]
while True:
    if start==arr1[-1]:
        break
    if start+s not in arr1:
        count+=1
    start+=s
print(count)
        