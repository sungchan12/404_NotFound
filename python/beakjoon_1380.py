scenario_num = 1
while True:
    steal_neckgirl_cnt = int(input())

    if steal_neckgirl_cnt == 0:
        break
    else:
        students = []
        for _ in range(steal_neckgirl_cnt):
            students.append(input())
        # print(girl_list)

        sinario_list = []
        for i in range(2*steal_neckgirl_cnt-1):
            st_num, sinario = input().split()
            sinario_list.append(int(st_num))
        # print(sinario_list)

        for student_num in sinario_list:
            if sinario_list.count(student_num) == 1:
                # print(student_num)
                index = student_num-1
                break
        print(scenario_num, students[index])
        scenario_num += 1