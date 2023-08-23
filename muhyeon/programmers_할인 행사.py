def solution(want, number, discount):
    result = 0
    # want 항목들이 discount에 모두 포함되어 있는 확인
    for w in want:
        if w not in discount:
            return result
    for i in range(len(discount)):
        if i + 10 > len(discount):
            break
        temp_count = 0
        for w, n in zip(want, number):
            if n <= discount[i:i+10].count(w):
                temp_count += 1
        if temp_count == len(want):
            result += 1
                
    return result
