import sys

input = sys.stdin.readline

n = int(input())
way = input().strip()
root = []
for i in range(n):
   row = []
   for j in range(n):
       row.append(".")
   root.append(row)

direction = {"U" : (-1, 0), "R" : (0, 1), "D" : (1, 0), "L" : (0, -1)}

sr, sc = 0, 0

for w in way:
    wr, wc = direction.get(w)
    move_sr, move_sc = (sr+wr), (sc+wc)
    # print(move_sr, move_sc)
    if (0 <= move_sr < n) and (0 <= move_sc < n):
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
        sr, sc = move_sr, move_sc
        # print(sr, sc)
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
for row in root:
   print(''.join(row))