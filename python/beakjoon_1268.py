stu_num = int(input())
students = []
for _ in range(stu_num):
    classes = list(map(int, input().split()))
    students.append(classes)

class_cnt = []
result = 0

for student_index in range(stu_num):
    cnt = 0
    for j in range(stu_num):
        if student_index != j:
            for grade in range(5):
                if students[student_index][grade] == students[j][grade]:
                    cnt += 1
                    break
    class_cnt.append(cnt)

print(class_cnt.index(max(class_cnt)) + 1)
