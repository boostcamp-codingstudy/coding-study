n=int(input())
array=[]
counts=[]
for i in range(n):
    array.append(int(input()))
array.sort()
for i in range(n):
    count=0
    for j in range(n):
        if array[j] in range(array[i],array[i]+5):
            count+=1
    counts.append(5-count)
print(min(counts))
