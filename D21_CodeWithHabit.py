# Zip function
daysCZE = ["pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota", "neděle"]
daysENG = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
daysNOR = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]
daysIND = ["senin", "selasa", "ribu", "kamis", "jumpat", "sabtu", "hari minggu"]

zipped = zip(daysCZE, daysENG, daysNOR, daysIND)
print(zipped)
zippedList = list(zipped)
print(zippedList)

for days in zippedList:
    print(days)

 