m = int(input())
s = []
# print(m)
for i in range(m):
    order = input().split()
    if len(order) == 1:
        string = order[0]
    else:
        string, num = order[0], order[1]
        # print(string, num)
    if string == 'add':
        if num not in s:
            s.append(num)
        else:
            pass
    if string == 'check':
        if num in s:
            print(1)
        else:
            print(0)
    if string == 'remove':
        try:
            s.remove(num)
        except ValueError:
            pass
    if string == 'togle':
        if num in s:
            s.remove(num)
        else:
            s.append(num)
    if string == 'empty':
        s.clear()
    if string =='all':
        s.sort()
# print(s)