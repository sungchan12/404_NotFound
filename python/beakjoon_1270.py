n = int(input())
land = []
for _ in range(n):
    land.append(list(map(int, input().split())))
for i in range(n):
    dic = {}
    temp = land[i][1:]
    for num in temp:
        # print(num)
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
        # print(dic)
    max_key = max(dic, key=dic.get)
    # print(dic[max_key])
    if dic[max_key] > land[i][0] / 2:
        print(max_key)
    else:
        print("SYJKGW")
# print(land)