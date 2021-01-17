# Datetime module
# built-in module
import datetime

today = datetime.date.today() # today`s date
birthdate = datetime.date(1990, 8, 31)

days_since_birth = today - birthdate # finding out how many days it is since your birhdate
print((days_since_birth).days) # same like above, but stating only days

tdelta = datetime.timedelta(days=300) # creating a timedelta of 300 days
print(tdelta)

future_date = today + tdelta # finding out what will be the date in 300 days
print(future_date)

# suggestion for other learning and exercises: create a time delta on hours, which module?

