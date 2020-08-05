#!/usr/bin/python3
#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly. 

#4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function. 
newpay = 0
pay = 0
extrah = 0
hours = input("Enter hours: ")
rate = input("Enter rate: ")
try:
    h = float(hours)
    r = float(rate)
except:
    print("Enter a valid number")
    quit()

def computepay(h, r):
    if h <= 40:
        pay = h*r
        return pay
    else:
        pay = 40*r
        extrah = h-40
        newpay = extrah*(r*1.5)
        h = pay+newpay
        return h

print("Pay", computepay(h, r))
