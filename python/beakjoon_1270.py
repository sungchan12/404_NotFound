n = int(input())
land = []
for _ in range(n):
    land.append(list(map(int, input().split())))
for i in range(n):
    dic = {}
    temp = land[i][1:]
    for num in temp:
        # print(num)
        if num in dic[num]:
            dic[num] += 1
        else:
            dic[num] = 1
        print(dic)
print(land)