n, m = map(int, input().split())
chess_color = []
for _ in range(n):
    chess_color.append(input())
# print(chess_color)
cnt = []
for column in range(n-7):
    for row in range(m-7):
        # print(column, row)
        white_cnt = 0
        black_cnt = 0
        for i in range(column, column + 8):
            for j in range(row, row + 8):
                if (i+j) % 2 == 0:
                    if chess_color[i][j] != 'W':
                        white_cnt += 1
                    else:
                        black_cnt += 1
                else:
                    if chess_color[i][j] != 'W':
                        black_cnt += 1
                    else:
                        white_cnt += 1
        cnt.append(white_cnt)
        cnt.append(black_cnt)
# print(cnt)
print(min(cnt))