import sys
input = sys.stdin.readline

def find_max(value):
    for i in range(n-value+1):
        for j in range(m-value+1):
            if s[i][j] == s[i+value-1][j] == s[i][j+value-1] == s[i+value-1][j+value-1]:
                return True
    return False

n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(input().strip()))

side = min(n, m)
for k in range(side, 0, -1):
    if find_max(k):
        print(k * k)
        break