filename = input("Enter the file name: ")
count = 0
dspam = 0
sumdspam = 0

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
        sumdspam = dspam + sumdspam
print("Average spam confidence:", format(sumdspam/count, '.12f'))

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print(line)
print("Done")

