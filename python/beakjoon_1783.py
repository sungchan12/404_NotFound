import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# direction = [(-2, 1), (-1, 2), (1, 2), (2, 1)]

# n == 1 어차피 1칸
if n == 1 or m == 1:
    print(1)
# n == 2 m >= 2 (-1, 2), (1, 2)만 가능
# n = 2, m = 2 1칸
# n = 2, m = 3 2칸
# n = 2, m = 4 2칸
# n = 2, m = 5 3칸
# n = 2, m = 6 3칸
# n = 2, m = 7 4칸
elif n == 2:
    print(min(4, (m + 1) // 2))
# m = 2 2칸
# m = 3 3칸
# m = 4 4칸
# m = 5 4칸
# m = 6 4칸
elif n >= 3:
    if m < 7:
        print(min(4, m))
# m = 7 5칸
# m = 8 6칸 
# m = 9 7칸
    elif m >= 7:
        print(m-2)