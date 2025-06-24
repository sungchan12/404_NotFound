import sys
input = sys.stdin.readline

def array_to_chess(row, col):
    chess_col = chr(ord('a') + col)
    chess_row = 8 - row
    return chess_col + str(chess_row)

# def 
chess_board = []

for _ in range(6):
    row = []
    for _ in range(6):
        row.append(0)
    chess_board.append(row)

print(chess_board)
for i in range(36):
    n = input().strip()
    row, column = n[1], n[0]
    # print(row, column)