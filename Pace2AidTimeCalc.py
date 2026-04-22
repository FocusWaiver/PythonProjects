# Footrace pace to real time calculator
import time

# givens, can eventually do input
start = time.strptime("Sat Aug 8 05:00:00 2026")
# min/mile
pace = 21
# miles between aidstations
aidst = [18.2, 25.4, 19.7, 17.6, 22.6]

# pace calculation
mph = (60 / pace)
# translate struct.time to epoch secs
timelist = [time.mktime(start)]

# find secs to next aidstation and append to timelist
for i in range(len(aidst)):
    sec = aidst[i] / mph * 60 * 60
    timenew = timelist[i] + sec
    timelist.append(timenew)

# convert each epoch sec to local time and print readout
for j in range(len(timelist) - 1):
    arrival = time.strftime("%b, %d, %H, %M", time.localtime(timelist[j + 1]))
    print("For crewed aid station: ", j + 1, "\nArrive around: ", arrival, "\n")

# To improve:
# could fix print format to make it easier to read. ie saving var from struct


