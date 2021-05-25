import datetime

date1 = datetime.date(2020,8,31)
print(date1)

date2 = datetime.date(2021,5,23)
print(date2)

delta = date2 - date1
print(delta)
print("It has been " + str(delta) + " days since my last birthday party.")


