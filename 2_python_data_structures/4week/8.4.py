#!/usr/bin/python3
# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order. You can download the sample data at http://www.py4e.com/code3/romeo.txt

filename = input("Enter file name: ")
#filename = "romeo.txt"
list_all = list()
list_new = list()

try:
    fh = open(filename)
except:
    print("File cannot be opened:", filename)
    quit()

for line in fh:
    line = line.rstrip()
    #print(line)
    listw = line.split()
    list_all = listw + list_all

list_all.sort()

for wordpos in range(len(list_all)):
    if list_all[wordpos] not in list_new:
        #print("Palavra",list_all[wordpos])
        #print("Lista",list_new)
        list_new.append(list_all[wordpos])

print(list_new)
