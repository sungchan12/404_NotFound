hurt_fin = int(input())
use_cnt = int(input())
# print(hurt_fin, use_cnt)
fin_cnt = 0
num = 0
finger = 0
direction = 1
while fin_cnt <= use_cnt:
    num += 1
    finger += direction
    if finger == 5:
        direction = -1
    elif finger == 1:
        direction = 1
    if finger == hurt_fin:
        fin_cnt += 1