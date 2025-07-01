import sys

input = sys.stdin.readline
n = int(input())
moves = input().strip()

# print(n, moves)

direction_x = [0, -1, 0, 1]
direction_y = [1, 0, -1, 0]

start_x, start_y= 0, 0
path = [(start_x, start_y)]
# print(path[0])
direction = 0
for move in moves:
    if move == "R":
        direction += 1
    elif move == "L":
        direction -= 1
    elif move == "F":
        start_x += direction_x[direction]
        start_y += direction_y[direction]
        path.append((start_x, start_y))
# print(path)
x_point = []
y_point = []
for p in path:
    # print(p[0])
    x_point.append(p[0])
    y_point.append(p[1])
# print(x_point)
# print(y_point)

maze = []
x_length = max(x_point) - min(x_point)+1
y_length = max(y_point) - min(y_point)+1
for i in range(x_length):
    row = []
    for j in range(y_length):
        row.append("#")
    maze.append(row)
# print(maze)
# 5 2x2
# RRFRF
# [0, 0, 1]
# [0, -1, -1]

# 6
# LFFRFF 3x3
# [0, 1, 2, 2, 2]
# [0, 0, 0, 1, 2]

# 19 4x4
# FLFRFFRFFFRFFRFLFLL
# [0, 0, 1, 1, 1, 0, -1, -2, -2, -2, -1, -1]
# [0, 1, 1, 2, 3, 3, 3, 3, 2, 1, 1, 0]