import sys

input = sys.stdin.readline
n = int(input())
status = list(map(int, input().split()))
# print("status : ", status)
student_num = int(input())
# print("student_num : ", student_num)
for _ in range(student_num):
    gender, switch = map(int, input().split())
    # print("gender : ", gender, " switch_num : ", switch)
    if gender == 1:
        for i in range(len(status)):
            if (i+1) % switch == 0:
                if status[i] == 0:
                    status[i] = 1
                else:
                    status[i] = 0
    else:
        center = switch-1
        left = center-1
        right = center+1
        
        status[center] = 1 - status[center]
        
        while (left >= 0 and right < n and status[left] == status[right]):
            if status[left] == 0:
                status[left] = 1
                status[right] = 1
            else:
                status[left] = 0
                status[right] = 0
            left -= 1
            right += 1
# print(status)
for i in range(len(status)):
    print(status[i], end=" ")
    if (i + 1) % 20 == 0:
        print()