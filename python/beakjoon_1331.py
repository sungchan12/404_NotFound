import sys
input = sys.stdin.readline

def array_to_chess(col, row):
    chess_row = 6 - row
    chess_colunm = chr(ord('a')+col)
    return chess_colunm, chess_row

def chess_to_index(n):
    chess_column = n[0].lower()
    chess_row = int(n[1])
    print(chess_column, chess_row)
    column = ord(chess_column)-ord('a')
    row = 6 - chess_row
    return column, row

chess_board = []
for _ in range(6):
    row = []
    for _ in range(6):
        row.append(0)
    chess_board.append(row)

for i in range(6):
    for j in range(6):
        if chess_board[i][j] == 0:
            chess_board[i][j] = array_to_chess(i, j)

print(chess_board)
for i in range(1):
    chess_to_index(input().strip())
    