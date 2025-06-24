import sys
input = sys.stdin.readline

# def index_to_chess(row, column):

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