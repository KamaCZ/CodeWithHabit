import calendar

calendar.setfirstweekday(0) # setting the first weekday for sunday

print(calendar.month(2021, 1, 3)) # printing a specified month of a yearr

print(calendar.weekheader(3)) # printing a weekheader

print(calendar.monthcalendar(2021, 1)) # printing a specific month of a year in the form of list of lists 

print(calendar.calendar(2021)) # printing calender of specified year

print(calendar.weekday(2021, 1, 8)) # printing the weekday of a specific date (0=Monday)

print(calendar.isleap(2021)) # printing True if the year is a leap year

print(calendar.leapdays(2021,2025)) # printing number of leap days between year 2021-2025, 2021 included, 2025 not

import datetime

print(datetime.date(2021, 1, 8)) # printing a specific date
print(datetime.date.today()) # printing today`s date
print(datetime.datetime.now())

