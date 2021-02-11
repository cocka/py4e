#!/usr/bin/python3
#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

filename = input("Enter file name: ")
list_all = list()
counts = dict()
count_hours = list()
hours2 = list()

if len(filename) < 1 :
    filename = "mbox-short.txt"

try:
    fh = open(filename)
except:
    print("File cannot be opened:", filename)
    quit()

for line in fh:
    if line.startswith('From '):
        line = line.rstrip()
        hours = line.split()
        hours = hours[5].split(':')
        hours = hours[0]
        #print("hours", hours)
        hours2.append(hours)

for hour in hours2:
   counts[hour] = counts.get(hour, 0 ) + 1
   #print(counts[hour])
#print("counts", counts)

for key, val in counts.items():
    newtup = (key, val)
    count_hours.append(newtup)

#print("count_hours", count_hours)
count_hours = sorted(count_hours)
#print("count_hours sorted", count_hours)

for key, val in count_hours:
    print(key, val)

