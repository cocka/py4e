#!/usr/bin/python3
# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order. You can download the sample data at http://www.py4e.com/code3/romeo.txt

filename = input("Enter file name: ")
list_all = list()
counts = dict()
bigcount = None
bigword = None

if len(filename) < 1 :
    filename = "mbox-short.txt"

try:
    fh = open(filename)
except:
    print("File cannot be opened:", filename)
    quit()

for line in fh:
    if line.startswith('From:'):
        line = line.rstrip()
        words = line.split()
        list_all.append(words[1])

for email in list_all:
    counts[email] = counts.get(email, 0) + 1
#print(counts)

for email,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = email
        bigcount = count

print(bigword, bigcount)

