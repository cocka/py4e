#!/usr/bin/python3

#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

number = None

def inputnumber():
    smallest = None
    largest = None
    while True:
        number = input("Enter a number: ")
        if number == 'done':
            break
        try:
            number = float(number)
        except:
            print("Invalid input")
            continue
        if smallest is None:
            smallest = number
        elif number < smallest:
            smallest = number
        #print(smallest)
        if largest is None:
            largest = number
        elif number > largest:
            largest = number
        #print(largest)
    print("Maximum is", int(largest))
    print("Minimum is", int(smallest))

inputnumber()
