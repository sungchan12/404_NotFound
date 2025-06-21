import sys
input = sys.stdin.readline

n, new_score, p = map(int, input().split())

if n == 0:
    print(1)
else:
    score_list = list(map(int, input().split()))
    if n == p and score_list[-1] >= new_score:
        print(-1)
    else:
        rank = 0
        for i in range(n):
            if score_list[i] > new_score:
                rank = i + 2
            else:
                rank = i + 1
                break
        else:
            rank = n + 1
        print(rank)