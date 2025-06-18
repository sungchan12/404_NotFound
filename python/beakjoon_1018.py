n, m = map(int, input().split())
chess_color = []
for _ in range(n):
    chess_color.append(input())
# print(chess_color)

for s in range(n-7):
    for e in range(m-7):
        #if chess_color[s][e] == 'W':
            # print("white")
        #else:
            #print("black")
        white_cnt = 0
        black_cnt = 0
        for k in range(s, s + 8):
            for l in range(e, e + 8):
                if (k+l)%2 == 0:
                    if chess_color[k][l] != 'W':
                        white_cnt += 1
                    else:
                        black_cnt += 1
                else:
                    if chess_color[k][l] != 'W':
                        black_cnt += 1
                    else:
                        white_cnt += 1
                        
print(min(white_cnt, black_cnt))
