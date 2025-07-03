

# ----------------- 내 코드 ----------------------
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
    for i in range(4):
        if direction[i] == 1:
            cogwheel[i] = [cogwheel[i][7]] + cogwheel[i][:7]
            # for line in cogwheel:
            #    print(line)
        elif direction[i] == -1:
            cogwheel[i] = cogwheel[i][1:] + [cogwheel[i][0]]
            # for line in cogwheel:
            #    print(line)
# for line in cogwheel:
#     print(line)
score = 0
for i in range(4):
    # print(line[0])
    if cogwheel[i][0] == 1:
        score += 2**i
    # if cogwheel[i][0] == 1:
    #     if i < 2:
    #         # print("%d 만큼 score에 더해졌습니다." % (i+1))
    #         score += (i+1)
    #     elif i == 2:
    #         # print("%d 만큼 score에 더해졌습니다." % (i+2))
    #         score += (i+2)
    #     else:
    #         # print("%d 만큼 score에 더해졌습니다." % 2*(i+1))
    #         score += 2*(i+1)
print(score)