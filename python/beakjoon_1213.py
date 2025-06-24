import sys
input = sys.stdin.readline

n = input().strip()
alpha_cnt = {}
# print(n)
for alpha in n:
    alpha_cnt[alpha] = alpha_cnt.get(alpha, 0) + 1
# print(alpha_cnt)
odd_cnt = 0
for num in alpha_cnt.values():
    if num % 2 == 1:
        odd_cnt += 1
if odd_cnt <= 1:
    # print("가능")
    front = ""
    middle =""
    for alpha in sorted(alpha_cnt.keys()):
        cnt = alpha_cnt[alpha]
        front += alpha * (cnt // 2)
        if cnt % 2 == 1:
            middle = alpha
    print(front + middle + front[::-1])
else:
    print("I'm Sorry Hansoo")