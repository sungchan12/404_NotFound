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
        direction = (direction + 1) % 4
    elif move == "L":
        direction = (direction - 1 + 4) % 4
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
for i in range(y_length):
    row = []
    for j in range(x_length):
        row.append("#")
    maze.append(row)

for x, y in path:
    x_path = x - min(x_point)
    y_path = y - min(y_point)

    maze[y_path][x_path] = "."

for line in maze:
    print("".join(line))