# Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the hour
# out from the 'From ' line by finding the time and then splitting the string a
# second time using a colon.
#     From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

# Reference: https://www.py4e.com/html3/10-tuples

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hoursDict = dict()
times = list()
for line in handle:
    words = line.split()
    for word in words:
        if word == "From":
            hourIndex = line.index("From") + 5
            temp = words[hourIndex].split(":")

            times.append(temp[0])

for time in times:
    if len(hoursDict) is 0:
        hoursDict[times[0]] =  0
    else:
        uniqueHour = True
        for hour in hoursDict:
            if time is hour:
                uniqueHour = False
                break

        if uniqueHour == True:
            hoursDict[time] = 0
            continue

for hour in hoursDict:
    for time in times:
        if time == hour:
            hoursDict[hour] += 1
        else:
            continue


lst = list(hoursDict.keys())
lst.sort()
for key in lst:
    print(key, hoursDict[key])
