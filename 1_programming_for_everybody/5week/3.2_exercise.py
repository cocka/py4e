#!/usr/bin/python3
#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly. 
newpay = 0
pay = 0
extrah = 0
hours = input("Enter hours: ")
rate = input("Enter rate: ")
try:
    h = float(hours)
    r = float(rate)
except:
    print("Erro")
    quit()

if h <= 40:
    pay = h*r
    print(pay)
else:
    pay = 40*r
    extrah = h-40
    newpay = extrah*(r*1.5)
    h = pay+newpay
    print(h)
