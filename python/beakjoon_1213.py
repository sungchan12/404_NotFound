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
    print("가능")
else:
    print("I'm Sorry Hansoo")