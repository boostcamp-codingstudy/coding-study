'''
1. 각각의 word를 구성 하는 alphabet의 문자 별 개수를 세어 "embeddings"라는 list에 저장
    예) 'GOOD' -> [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
2. 첫 번째 단어의 embedding을 기준으로 나머지 단어의 embedding을 순회 하면서 두 단어 embedding의 각 원소의 차이를 제곱 해서 합 한 결과를 "difference"라는 변수에 저장
3. difference가 2 보다 크거나 어느 한 쪽이 2 개 이상 문자가 많은 경우, 비슷한 단어에서 제외
'''
def solution():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())

    capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    embeddings = [[0 for e in range(len(capitals))] for _ in range(n)]

    for i in range(n):
        for c in words[i]:
            embeddings[i][ord(c) - 65] += 1

    count = 0
    for i in range(1, n):
        difference = 0
        for j in range(len(capitals)):
            difference += pow(embeddings[0][j] - embeddings[i][j], 2)
        if difference < 3 and abs(sum(embeddings[0]) - sum(embeddings[i])) < 2:
            count += 1

    print(count)

solution()
