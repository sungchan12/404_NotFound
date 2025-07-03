cogwheel = [] # 톱니바퀴 s면 1 n이면 0
for _ in range(4):
    cogwheel.append(list(map(int, input())))
# print(cogwheel)

k = int(input()) # 회전횟수
for _ in range(k):
    # roate_direction이 1이면 시계방향, -1이면 반시계 방향
    cog_num, roate_direction = map(int, input().split())
    cog_index = cog_num-1
    direction = [0] * 4
    direction[cog_index] = roate_direction
    # print(cog_num, roate_direction)
    # print(cogwheel[cog_num])
# (0, 2) (1, 6) / (1, 2) (2, 6) / (2, 2) (3, 6) /
    # 오른쪽 검사
    for i in range(cog_index, 3):
        if cogwheel[i][2] != cogwheel[i+1][6]:
            direction[i+1] = -direction[i] 
        else:
            break 
    # 왼쪽 검사
    for i in range(cog_index, 0, -1):
        if cogwheel[i][6] != cogwheel[i-1][2]:
            direction[i-1] = -direction[i]
        else:
            break
    # print(direction)