import sys
input = sys.stdin.readline
n = int(input().strip())
num_list = []

for _ in range(n):
    num_list.append(int(input().strip()))
print(num_list)

if len(num_list) < 5:
    print(5-len(num_list))