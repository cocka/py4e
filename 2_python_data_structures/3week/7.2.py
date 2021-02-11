#!/usr/bin/python3

filename = input("Enter the file name: ")
count = 0
dspam = 0
somadspam = 0

try:
    if filename == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        file = open(filename)
except:
    print("File cannot be opened:", filename)

for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        line = line.rstrip()
        linepos = line.find(':')
        dspam = line[linepos+1:]
        dspam = float(dspam)
        count = count + 1
        somadspam = dspam + somadspam
print("Average spam confidence:", round(somadspam/count, 12))
