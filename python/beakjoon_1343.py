n = input()

pure_x = n.split(".")
# print(pure_x)
change_x = []
can_print = True
for x in pure_x:
    cnt = len(x)
    # print(cnt)
    if (cnt % 2 != 0):
        can_print = False
        break
    elif (cnt % 4) == 0:
        change_x.append('AAAA'*(cnt//4))
    else:
        change_x.append('AAAA'*(cnt//4) + 'BB')

if can_print:
    result = ".".join(change_x)
    print(result)
else:
    print(-1)