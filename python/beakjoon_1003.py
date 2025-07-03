import sys

def fibonacci(num):
    global zero_cnt, one_cnt
    if num == 0:
        zero_cnt += 1
        return 0
    elif num == 1:
        one_cnt += 1
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())

    zero_cnt = 0
    one_cnt = 0

    fibonacci(num)
    
    print(zero_cnt, one_cnt)