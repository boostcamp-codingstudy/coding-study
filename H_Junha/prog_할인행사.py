def solution(want, number, discount):
    answer = 0
    ten_days = []
    for i in range(len(discount) - 9):
        ten_days = discount[i:i+10]
        new_num = number[:]
        for obj in ten_days:
            if obj in want:
                if new_num[want.index(obj)] != 0:
                    new_num[want.index(obj)] -= 1

        if sum(new_num) == 0:
            answer += 1
            
    return answer