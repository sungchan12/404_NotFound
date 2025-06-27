import sys

input = sys.stdin.readline

month, day, year, time = input().split()
day = int(day[:-1])
year = int(year)
minutes, second = map(int, time.split(":"))

