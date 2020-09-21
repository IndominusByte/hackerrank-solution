year = 1918
gregorian_day = 244 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 243
if year == 1918:
    print("{}.09.{}".format(256 - gregorian_day + 13,year))
if year < 2000 and year % 100 == 0:
    print("{}.09.{}".format(12,year))
print("{}.09.{}".format(256 - gregorian_day,year))
