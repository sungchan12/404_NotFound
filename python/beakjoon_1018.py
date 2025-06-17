n, m = map(int, input().split())
chess_color = []
for _ in range(n):
    chess_color.append(input())
# print(chess_color)

for start in range(n-7):
    for end in range(m-7):
        for i in range(8):
            for j in range(8):
                