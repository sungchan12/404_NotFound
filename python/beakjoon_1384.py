group_cnt = 1
n = int(input())
student_list = []
nasty_reports = []

for i in range(n):
    parts = input().split()
    student_list.append(parts[0])
    nasty_reports.append(parts[1:])
# print(student_list)
# print(nasty_reports)

