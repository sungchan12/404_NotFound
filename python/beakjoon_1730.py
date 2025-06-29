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

direction = {"U" : (-1, 0), "R" : (0, 1), "D" : (1, 0), "L" : (0, -1)}

sr, sc = 0, 0

for w in way:
    # print(w)
    if w == "D":
        wr, wc = direction.get(w)
        # print(wr, wc)
        sr += wr
        sc += wc