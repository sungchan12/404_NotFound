n = int(input())
number_list = []
cnt = 0
for _ in range(n):
    number_list.append(str(input()))
print(number_list)
for i in range(1, len(number_list[0])+1):
    temp = set()
    for number in number_list:
        cut = number[-i:]
        temp.add(cut)
    # print(temp)
    if len(temp) == n:
        print(len(temp))
        break