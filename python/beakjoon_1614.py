import sys

hurt_fin = int(sys.stdin.readline()) # 다친 손가락
use_cnt = int(sys.stdin.readline()) # 다친 손가락 사용 횟수
# print(hurt_fin, use_cnt)
# fin_cnt = 0
# num = 0
# finger = 0
# direction = 1
# while fin_cnt <= use_cnt:
#     num += 1
#     finger += direction
#     if finger == hurt_fin:
#         fin_cnt += 1    
#     if finger == 5:
#         direction = -1
#     elif finger == 1:
#         direction = 1
# print(num-1)
num = 0
if use_cnt == 0:
    if hurt_fin == 1:
        print(0)
    else:
        print(hurt_fin-1)
else:
    if hurt_fin == 5:
        num += use_cnt * 8
        num += 4   
    elif hurt_fin == 1:
        num += use_cnt * 8
    else:
        full_cycles = use_cnt // 2
        num += full_cycles * 8 
        remain_cnt = use_cnt % 2
        if remain_cnt == 1:
            num += (8 - (hurt_fin-1))
        else:
            num += hurt_fin-1
    print(num)