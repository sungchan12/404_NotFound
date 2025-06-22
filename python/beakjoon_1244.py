import sys

input = sys.stdin.readline
n = int(input())
status = list(map(int, input().split()))
print("status : ", status)
student_num = int(input())
print("student_num : ", student_num)
for _ in range(student_num):
    gender, switch = map(int, input().split())
    print("gender : ", gender, " switch_num : ", switch)
    if gender == 1:
        for i in range(len(status)):
            if (i+1) % switch == 0:
                if status[i] == 0:
                    status[i] = 1
                else:
                    status[i] = 0
print(status)