import sys
input = sys.stdin.readline
n = int(input().strip())
num_list = []
cnt = 0
for _ in range(n):
    num_list.append(int(input().strip()))
num_list.sort()
print(num_list)

if len(num_list) < 5:
    print(5-len(num_list))

for i in range(len(num_list)):
    print(i)
    if num_list[i+1] - num_list[i] == 1:
        print(num_list[i+1], num_list[i])
        cnt += num_list[i+1] - num_list[i] -1
print(cnt)