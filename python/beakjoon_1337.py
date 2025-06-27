import sys
input = sys.stdin.readline
n = int(input().strip())
num_list = []
cnt_list = []
for _ in range(n):
    num_list.append(int(input().strip()))
# print(num_list)

for i in range(0, len(num_list)):
    # print(num_list[i])
    cnt = 0
    for j in range(num_list[i], num_list[i]+5):
        if j not in num_list:
            cnt += 1
    cnt_list.append(cnt)
print(min(cnt_list))