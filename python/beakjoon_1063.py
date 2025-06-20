import sys

input = sys.stdin.readline
king_info, stone, loop = input().split()
king_info = king_info.lower()
stone = king_info.lower()
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

def get_king_index(king_info):
    row = int(king_info[1])
    column = king_info[0]
    # print(column, row)
    return_col = ord(column) - ord('a')
    return_row = 8 - row
    return return_col, return_row

for i in range(8):
    for j in range(8):
        if chess_board[i][j] == 0:
            chess_board[i][j] = array_to_chess(i, j)

# print(chess_board)
# print(get_king_index(king_info))
x, y = map(int, get_king_index(king_info))

for _ in range(loop):
    order = input().strip()
    # print(x, y)
    if order == 'B':
        if x <= 0 or y >= 7:
            pass
    else:
        y += 1
        # print(x, y)
        # print(array_to_chess(y, x))