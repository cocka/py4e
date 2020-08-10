#!/usr/bin/python3
# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order. You can download the sample data at http://www.py4e.com/code3/romeo.txt

filename = input("Enter file name: ")
list_all = list()
list_new = list()
count = 0

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
        count = count+1
        print(words[1])

print("There were", count, "lines in the file with From as the first word")
