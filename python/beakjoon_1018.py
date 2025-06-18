n, m = map(int, input().split())
chess_color = []
for _ in range(n):
    chess_color.append(input())
# print(chess_color)

for s in range(n-7):
    for e in range(m-7):
        if chess_color[s][e] == 'W':
            print("white")
        elif chess_color[s][e] == 'B':
            print("black")
        for k in range(s + 7):
            for l in range(e + 7):
                if (s+e)%2 == 0:
                    