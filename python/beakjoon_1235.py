n = int(input())
number = []
cnt = 0
for _ in range(n):
    num = str(input())
    number.append(int(num[4:7]))
print(number)
temp = []
for i in range(len(number)):
    if number[i] in temp:
        pass
    else:
        temp.append(number[i])
print(len(temp))