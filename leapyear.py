import calendar
from datetime import datetime
current_year = datetime.now().year
end_year = int(input("Enter the year to check for future leap years: "))
def is_leap_year(year):
    return calendar.isleap(year)
print("Future leap years from {current_year} to {end_year} are:")
for year in range(current_year + 1, end_year + 1):
    if is_leap_year(year):
        print(year)


