import sys

input = sys.stdin.readline
king_info, stone_info, loop = input().split()
king_info = king_info.lower()
stone_info = stone_info.lower()
loop = int(loop)

chess_board = []
for _ in range(8):
    row = []
    for _ in range(8):
        row.append(0)
    chess_board.append(row)

def array_to_chess(row, col):
    chess_col = chr(ord('a') + col)
    chess_row = 8 - row
    return chess_col + str(chess_row)

def get_index(info):
    row = int(info[1])
    column = info[0]
    return_col = ord(column) - ord('a')
    return_row = 8 - row
    return return_col, return_row

for i in range(8):
    for j in range(8):
        if chess_board[i][j] == 0:
            chess_board[i][j] = array_to_chess(i, j)

king_x, king_y = map(int, get_index(king_info))
stone_x, stone_y = map(int, get_index(stone_info))
# print("king_x : ", king_x, " king_y : ", king_y)
# print("stone_x : ", stone_x, " stone_y : ", stone_y)

for _ in range(loop):
    order = input().strip()
    # 오른쪽으로
    if order == 'R':
        new_king_x = king_x + 1
        if new_king_x > 7:
            pass
        elif new_king_x == stone_x and king_y == stone_y:
            new_stone_x = stone_x + 1
            if new_stone_x > 7:
                pass
            else:
                king_x = new_king_x
                stone_x = new_stone_x
        else:
            king_x = new_king_x
            
    # 왼쪽으로
    elif order == 'L':
        new_king_x = king_x - 1
        if new_king_x < 0:
            pass
        elif new_king_x == stone_x and king_y == stone_y:
            new_stone_x = stone_x - 1
            if new_stone_x < 0:
                pass
            else:
                king_x = new_king_x
                stone_x = new_stone_x
        else:
            king_x = new_king_x
            
    # 한 칸 아래로
    elif order == 'B':
        new_king_y = king_y + 1
        if new_king_y > 7:
            pass
        elif king_x == stone_x and new_king_y == stone_y:
            new_stone_y = stone_y + 1
            if new_stone_y > 7:
                pass
            else:
                king_y = new_king_y
                stone_y = new_stone_y
        else:
            king_y = new_king_y
            
    # 한 칸 위로
    elif order == 'T':
        new_king_y = king_y - 1
        if new_king_y < 0:
            pass
        elif king_x == stone_x and new_king_y == stone_y:
            new_stone_y = stone_y - 1
            if new_stone_y < 0:
                pass
            else:
                king_y = new_king_y
                stone_y = new_stone_y
        else:
            king_y = new_king_y
            
    # 오른쪽 위 대각선으로
    elif order == "RT":
        new_king_x = king_x + 1
        new_king_y = king_y - 1
        if new_king_x > 7 or new_king_y < 0:
            pass
        elif new_king_x == stone_x and new_king_y == stone_y:
            new_stone_x = stone_x + 1
            new_stone_y = stone_y - 1
            if new_stone_x > 7 or new_stone_y < 0:
                pass
            else:
                king_x = new_king_x
                king_y = new_king_y
                stone_x = new_stone_x
                stone_y = new_stone_y
        else:
            king_x = new_king_x
            king_y = new_king_y
            
    # 왼쪽 위 대각선
    elif order == "LT":
        new_king_x = king_x - 1
        new_king_y = king_y - 1
        if new_king_x < 0 or new_king_y < 0:
            pass
        elif new_king_x == stone_x and new_king_y == stone_y:
            new_stone_x = stone_x - 1
            new_stone_y = stone_y - 1
            if new_stone_x < 0 or new_stone_y < 0:
                pass
            else:
                king_x = new_king_x
                king_y = new_king_y
                stone_x = new_stone_x
                stone_y = new_stone_y
        else:
            king_x = new_king_x
            king_y = new_king_y
            
    # 오른쪽 대각선 아래
    elif order == "RB":
        new_king_x = king_x + 1
        new_king_y = king_y + 1
        if new_king_x > 7 or new_king_y > 7:
            pass
        elif new_king_x == stone_x and new_king_y == stone_y:
            new_stone_x = stone_x + 1
            new_stone_y = stone_y + 1
            if new_stone_x > 7 or new_stone_y > 7:
                pass
            else:
                king_x = new_king_x
                king_y = new_king_y
                stone_x = new_stone_x
                stone_y = new_stone_y
        else:
            king_x = new_king_x
            king_y = new_king_y
            
    # 왼쪽 대각선 아래
    elif order == "LB":
        new_king_x = king_x - 1
        new_king_y = king_y + 1
        if new_king_x < 0 or new_king_y > 7:
            pass
        elif new_king_x == stone_x and new_king_y == stone_y:
            new_stone_x = stone_x - 1
            new_stone_y = stone_y + 1
            if new_stone_x < 0 or new_stone_y > 7:
                pass
            else:
                king_x = new_king_x
                king_y = new_king_y
                stone_x = new_stone_x
                stone_y = new_stone_y
        else:
            king_x = new_king_x
            king_y = new_king_y

print(array_to_chess(king_y, king_x).upper())
print(array_to_chess(stone_y, stone_x).upper())