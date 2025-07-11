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
    
    # nasty 메시지가 있었는지 확인하기 위한 플래그
    was_nasty = False
    print("Group %d" % group_cnt)

    for i in range(n):
        for j in range(len(nasty_reports[i])):
            if nasty_reports[i][j] == "N":
                # 1. 보낸 사람의 '인덱스'를 계산
                sender_index = (i - j - 1 + n) % n
                
                # 2. 계산된 인덱스를 사용해 리스트에서 '이름'을 찾음
                sender_name = student_list[sender_index]
                
                print("%s was nasty to %s" % (sender_name, student_list[i]))
                was_nasty = True

    if not was_nasty: # nasty 메시지가 한 번도 없었다면
        print("Nobody was nasty")
    
    print() # 그룹 간 줄바꿈
    group_cnt += 1