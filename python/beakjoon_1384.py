group_cnt = 1
while True:
    n = int(input())
    if n == 0:
        break

    student_list = []
    nasty_reports = []

    for i in range(n):
        parts = input().split()
        student_list.append(parts[0])
        nasty_reports.append(parts[1:])
    # print(student_list)
    # print(nasty_reports)
    cnt = 0
    print("Group %d" % group_cnt)
    for i in range(n):
        for j in range(len(nasty_reports[i])):
            if nasty_reports[i][j] == "N":
                # print(i, j)
                if i > j:
                    name = student_list[i - (j+1)]
                else:
                    name = student_list[len(student_list) - (j+1)]
                print("%s was nasty to %s" % (name, student_list[i]))
                cnt += 1
    group_cnt += 1
    if cnt == 0:
        print("Nobody was nasty")
    print()