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
