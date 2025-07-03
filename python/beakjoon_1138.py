n = int(input())
tall_input = list(map(int, input().split()))
# print(tall_input)
tall_list = [0] * n

for i in range(len(tall_list)): # i = 0
    tall_num = tall_input[i]
    zero_cnt = 0
    for j in range(len(tall_list)):
        if tall_list[j] == 0:
            if zero_cnt == tall_num:
                tall_list[j] = i+1
                break
            zero_cnt += 1
print(*tall_list)