# 
T = int(input()) # Test의 갯수

for _ in range(T): 
    # W는 쓰레기차 용량
    # N은 지점의 갯수
    W, N = map(int, input().split())
    distance = []
    total_km = 0
    currnet_gar = 0
    location = 0
    for _ in range(N):
        # x_i = 쓰레기장으로부터의 거리
        # w_i = 쓰레기의 양
        x_i, w_i = map(int, input().split())
        distance.append((x_i, w_i))
    # print(distance[0])
    for x, w in distance:
        print("x : %d, w : %d" % (x, w))
        print("currnet_gar + w : %d" % (currnet_gar + w))
        if currnet_gar + w > W:
            location = x
            total_km += location * 2
            currnet_gar = w
            print("total_km : %d " % total_km)
        elif currnet_gar + w == W:
            total_km += x * 2
            currnet_gar = 0
            location = 0
            print("total_km : %d " % total_km)
        else:
            location = x
            currnet_gar += w
            print("total_km : %d " % total_km)
    if currnet_gar > 0:
        total_km += location * 2
        print("location : %d, currnet_gar : %d" % (location, currnet_gar))
    print("total_km : %d" % total_km)