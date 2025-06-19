import sys

input = sys.stdin.readline
king_info, stone, loop = input().split()
loop = int(loop)
# print(king_info, stone, loop)
chess_board = []
for _ in range(8):
    row = []
    for _ in range(8):
        row.append(0)
    chess_board.append(row)
# print(chess_board)

def array_to_chess(row, col):
    chess_col = chr(ord('a') + col)  
    chess_row = 8 - row             
    return chess_col + str(chess_row)
 
for i in range(8):
    for j in range(8):
        if chess_board[i][j] == 0:
            chess_board[i][j] = array_to_chess(i, j)
# print(chess_board)