import sys
input = sys.stdin.readline

# def array_to_chess(col, row):
#     chess_row = 6 - row
#     chess_colunm = chr(ord('a')+col)
#     return chess_colunm, chess_row

def chess_to_index(n):
    chess_column = n[0].lower()
    chess_row = int(n[1])
    # print(chess_column, chess_row)
    column = ord(chess_column)-ord('a')
    row = 6 - chess_row
    return column, row

def check(before, now):
    before_column, before_row = chess_to_index(before)
    now_column, now_row = chess_to_index(now)
    # print(now_column, now_row)
    knight_moves = [
        (1, -2), (1, 2),
        (-1, -2), (-1, 2),
        (2, -1), (2, 1),
        (-2, -1), (-2, 1)
    ]
    for move_column, move_row in knight_moves:
        move_column = before_column + move_column
        move_row = before_row + move_row

        if move_column == now_column and move_row == now_row:
            return True
    return False

chess_board = []
for _ in range(6):
    row = []
    for _ in range(6):
        row.append(0)
    chess_board.append(row)

# for i in range(6):
#     for j in range(6):
#         if chess_board[i][j] == 0:
#             chess_board[i][j] = array_to_chess(i, j)

# print(chess_board)

log = []
for i in range(36):
    n = input().strip()
    log.append(n)
    
valid_check = True
for i in range(len(log)):
    if i >= 1:
        if not check(log[i-1], log[i]):
            valid_check = False
            break
