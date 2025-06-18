import sys

input = sys.stdin.readline
king_info, stone, loop = input().split()
loop = int(loop)
# print(king_info, stone, loop)
chess_board = []
for i in range(8):
    row = []
    for j in range(8):
        row.append(0)
    chess_board.append(row)

def 