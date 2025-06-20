import sys

input = sys.stdin.readline
king_info, stone_info, loop = input().split()
king_info = king_info.lower()
stone = stone_info.lower()
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

def get_index(info):
    row = int(info[1])
    column = info[0]
    # print(column, row)
    return_col = ord(column) - ord('a')
    return_row = 8 - row
    return return_col, return_row

for i in range(8):
    for j in range(8):
        if chess_board[i][j] == 0:
            chess_board[i][j] = array_to_chess(i, j)
# print(chess_board)

king_x, king_y = map(int, get_index(king_info))
stone_x, stone_y = map(int, get_index(stone))
print("king_x : ", king_x, " king_y : ", king_y)
print("stone_x : ", stone_x, " stone_y : ", stone_y)

for _ in range(loop):
    order = input().strip()
    # print(x, y)
    if order == 'B':
        if king_y >= 7:
            pass
    else:
        king_y += 1
        # print(x, y)
        # print(array_to_chess(y, x))