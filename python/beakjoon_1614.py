import sys

hurt_fin = int(sys.stdin.readline()) # 다친 손가락
use_cnt = int(sys.stdin.readline()) # 사용 횟수
# print(hurt_fin, use_cnt)
fin_cnt = 0
num = 0
finger = 0
direction = 1
while fin_cnt <= use_cnt:
    num += 1
    finger += direction
    if finger == hurt_fin:
        fin_cnt += 1    
    if finger == 5:
        direction = -1
    elif finger == 1:
        direction = 1
print(num-1)