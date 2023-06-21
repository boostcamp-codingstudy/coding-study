'''

'''
import sys

def myRound(n):
    integer = int(n)
    floating = n - int(n)
    return integer + 1 if floating >= 0.5 else integer

def solution():
    n = int(input())
    scores = []
    for _ in range(n):
        scores.append(int(sys.stdin.readline().rstrip()))
    
    if n == 0: return print(0)
    
    scores.sort()
    n_outs = myRound(n * .15)
    scores = scores[n_outs:n - n_outs]
    print(myRound(sum(scores) / (n - 2 * n_outs)))

solution()