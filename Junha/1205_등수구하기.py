input_1 = list(map(int,input().split()))

N = input_1[0] # 리스트의 점수 개수
score = input_1[1]
P = input_1[2] #올라갈수 있는 점수의 개수

if N != 0:
    rank_list = sorted(list(map(int, input().split())) + [score], reverse=True)

    answer = rank_list.index(score)+1

    if answer > P:
        print(-1)
    else:
        if N == P and rank_list[-1] == score:
            print(-1)
        else:
            print(answer)
    
else:
    print(1)
    