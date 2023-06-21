'''
1. 입력에 존재 하는 문자의 집합 저장
2. 집합 내 문자 별 개수를 dictionary 저장
3. 문자 개수가 홀수이면 그 중 하나를 중심에 배치
3-1. 하나를 제외한 나머지 문자는 반개수 대칭 영역에 배치
3-2. 문자 개수가 홀수인 경우가 둘 이상이면 동작 중단
4. 문자의 개수가 짝수이면 반개수 대칭 영역에 배치
5. 중심을 기준으로 반개수를 대칭 하도록 출력
'''
def solution():
    s = input()
    a, d = list(set(s)), {}
    for c in a: d[c] = s.count(c)
    n, m, h = 0, [], []
    for k, v in d.items():
        if v % 2 == 1:
            if n == 0:
                m, n = [k], 1
                if v > 2: h += [k] * (v // 2)
            else: return print("I'm Sorry Hansoo")
        else: h += [k] * (v // 2)
    h.sort()
    print(''.join(h + m + h[::-1]))

solution()