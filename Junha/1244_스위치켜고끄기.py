num_switch = int(input())
switch = list(map(int, input().split()))
num_student = int(input())

for i in range(num_student):
    student = list(map(int,input().split())) # 성별, 받은 수
    
    if student[0] == 1:
        for n in range(student[1],num_switch+1,student[1]):
            switch[n-1] = int(not(switch[n-1]))
    else:
        switch[student[1]-1] = int(not(switch[student[1]-1]))
        left = student[1] - 1
        right = student[1] + 1
        if left >= 1 and right <= num_switch:    
            while switch[left-1] == switch[right-1]:
                switch[left-1] = int(not(switch[left-1]))
                switch[right-1] = int(not(switch[right-1]))
                left -= 1
                right += 1
                
                if left < 1 or right > num_switch:
                    break

for idx,s in enumerate(switch):
    print(s,end=" ")
    if (idx+1) % 20 == 0:
        print()
            