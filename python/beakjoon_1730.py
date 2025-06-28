import sys

input = sys.stdin.readline

n = int(input())
way = input().strip()
# print(len(way))
root = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(".")
    root.append(row)
# print(root)