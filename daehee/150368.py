def bruteforce(depth, case):
    if depth > items:
        cases.append([e for e in case])
        return
    for r in rates:
        case.append(r)
        bruteforce(depth + 1, case)
        case.pop()

def solution(users, emoticons):
    global rates
    global items
    global cases
    rates = [10, 20, 30, 40]
    items = len(emoticons)
    cases = []
    bruteforce(1, [])
    
    results = []
    for c in cases:
        joins = 0
        payments = 0
        for u in users:
            payment = 0
            for i in range(items):
                if c[i] >= u[0]:
                    payment += emoticons[i] * (100.0 - c[i]) / 100.0
            if payment >= u[1]:
                joins += 1
            else:
                payments += payment
        results.append([joins, payments])
    return sorted(results, key=lambda x : (-x[0], -x[1]))[0]


# checking answers
TCs = [
    (([[40, 10000], [25, 10000]], [7000, 9000]), ([1, 5400])), 
    (([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]), ([4, 13860]))
]
for i, (input, output) in enumerate(TCs):
    assert solution(*input) == output, f'TC#{i}incorrect\ninput:{input}\noutput:{output}'