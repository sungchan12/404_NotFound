t = int(input())
zero_cnt = [0] * 41
one_cnt = [0] * 41
# print(zero_cnt)
# print(one_cnt)

for _ in range(t):
    num = int(input())
    zero_cnt[0], one_cnt[0] = 1, 0
    zero_cnt[1], one_cnt[1] = 0, 1

    for i in range(2, num+1):
        zero_cnt[i] = zero_cnt[i-1] + zero_cnt[i-2]
        one_cnt[i] = one_cnt[i-1] + one_cnt[i-2]

    print(zero_cnt[num], one_cnt[num])