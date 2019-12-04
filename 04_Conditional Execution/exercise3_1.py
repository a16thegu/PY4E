# Write a program to prompt the user for hours and rate per hour using input
# to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times
# the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate
# of 10.50 per hour to test the program (the pay should be 498.75). You should
# use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types
# numbers properly.

# Then rewrite your pay program using try and except so that your program
# handles non-numeric input gracefully.

# Reference: https://www.py4e.com/html3/03-conditional

hrs = input("Enter Hours: ")
# h = float(hrs)

rate = input("Enter Rate: ")
# r = float(rate)

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input.")
    quit()

if h <= 40:
    pay = h * r

else:
    overtime = h - 40
    pay = (40 * r)  + 1.5 * (overtime * r)

print(pay)
