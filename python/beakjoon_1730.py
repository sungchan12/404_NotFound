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
    wr, wc = direction.get(w)
    # print(wr, wc)
    if w in "UD":
        if root[sr][sc] == ".":
            root[sr][sc] = "|"
        elif root[sr][sc] == "-":
            root[sr][sc] = "+"
    else:
        if root[sr][sc] == ".":
            root[sr][sc] = "-"
        elif root[sr][sc] == "|":
            root[sr][sc] = "+"
    sr += wr
    sc += wc
    if (sr < 0 or sr >= n) or (sc < 0 or sc >= n):
        sr = sr - wr
        sc = sc - wc
    else:
        if w in "UD":
            if root[sr][sc] == ".":
                root[sr][sc] = "|"
            elif root[sr][sc] == "-":
                root[sr][sc] = "+"
        else:
            if root[sr][sc] == ".":
                root[sr][sc] = "-"
            elif root[sr][sc] == "|":
                root[sr][sc] = "+"

# print(sr, sc)
for row in root:
   print(''.join(row))