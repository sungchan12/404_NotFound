import sys

input = sys.stdin.readline

month, day, year, time = input().split()
day = int(day[:-1])
year = int(year)
hours, minutes = map(int, time.split(":"))

months = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total = 365

def check_yoon(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if check_yoon(year):
    days[1] = 29
    total = 366

# print(days[1], total)

days_sum = day-1
for i in range(months.get(month)-1):
    days_sum += days[i]

total_sec = total * 24 * 60 * 60
total_day_sec = days_sum * 24 * 60 * 60
current_time_sec = (minutes * 60)

elapsed_sec = total_day_sec + current_time_sec
progress = (elapsed_sec / total_sec) * 100
print(progress)