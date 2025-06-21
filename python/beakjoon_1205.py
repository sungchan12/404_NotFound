import sys
input = sys.stdin.readline

n, new_score, p = map(int, input().split())

if (n == 0):
    print(1)
else:
    score_list = list(map(int, input().split()))
    score_list.sort(reverse=True)
    result = 0
    if score_list[-1] == new_score:
        print(-1)
    else: 
        for i in range(len(score_list)):
            if score_list[i] <= new_score:
                result = i+1
                print(result)
                break
            
    # print(n, new_score, p)
    # print(score_list)
