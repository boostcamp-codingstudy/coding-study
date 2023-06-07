1. 각각의 word를 구성 하는 alphabet의 문자 별 개수를 세어 "embeddings"라는 list에 저장
    예) 'GOOD' -> [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
2. 첫 번째 단어의 embedding을 기준으로 나머지 단어의 embedding을 순회 하면서 두 단어 embedding의 각 원소의 차이를 제곱 해서 합 한 결과를 "difference"라는 변수에 저장
3. difference가 2 보다 크거나 어느 한 쪽이 2 개 이상 문자가 많은 경우, 비슷한 단어에서 제외