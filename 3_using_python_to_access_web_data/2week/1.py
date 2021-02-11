#!/usr/bin/python3
# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers. 
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

#import regex library
import re

#variables declaration
filename = input("Enter file name: ")
count = None
soma = 0

#opend a default file if none is passed
if len(filename) < 1 :
    filename = "sample.txt"

#check if the file can be opened
try:
    fh = open(filename)
except:
    print("File cannot be opened:", filename)
    quit()

#read each line
for line in fh:
    line = line.rstrip()
    #look for numbers in each line, and we are going to have a list for each line
    match = re.findall('[0-9]+', line)
    #if match is different from 0, if we have a list with content, sum the content
    if match != 0:
        #read the sublist from the list match
        for single in match:
            number = int(single)
            soma = number + soma

print(soma)

