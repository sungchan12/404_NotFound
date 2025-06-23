import sys
input = sys.stdin.readline

n = input().strip()
alpha_cnt = {}
# print(n)
for alpha in n:
    alpha_cnt[alpha] = alpha_cnt.get(alpha, 0) + 1
print(alpha_cnt)