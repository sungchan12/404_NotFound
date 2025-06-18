import sys
input = sys.stdin.readline

m = int(input())
s = set()

for i in range(m):
    order = input().split()
    if len(order) == 1:
        string = order[0]
    else:
        string, num = order[0], int(order[1])
    
    if string == 'add':
        s.add(num)
    elif string == 'check':
        print(1 if num in s else 0)
    elif string == 'remove':
        s.discard(num)
    elif string == 'toggle':
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif string == 'empty':
        s.clear()
    elif string == 'all':
        s = set(range(1, 21))