import datetime as dt

sundays = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if dt.datetime(year, month, 1).weekday() == 6:
            sundays += 1

print(sundays)
