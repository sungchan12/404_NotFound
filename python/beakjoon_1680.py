# 
T = int(input()) # Test의 갯수

for _ in range(T): 
    # W는 쓰레기차 용량
    # N은 지점의 갯수
    W, N = map(int, input().split())
    distance = []
    total_km = 0
    for i in range(N):
        # x_i = 쓰레기장으로부터의 거리
        # w_i = 쓰레기의 양
        x_i, w_i = map(int, input().split())
        distance.append([x_i, w_i])
        
    
    # print(distance)