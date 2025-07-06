import sys

n_str = sys.stdin.readline().strip()
n_int = int(n_str)
length = len(n_str)

ans = 0

for i in range(1, length):
    num_count = 9 * (10**(i-1))
    ans += num_count * i

ans += (n_int - (10**(length-1)) + 1) * length

print(ans)