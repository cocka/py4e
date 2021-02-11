#!/usr/bin/python3

filename = input("Enter a file name: ")
try:
    file = open(filename)
except:
    print("This file does not exist:", filename)
    quit()

for line in file:
    line = line.rstrip().upper()
    print(line)
