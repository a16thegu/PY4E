# Write a program that repeatedly prompts a user for integer numbers until the
# user enters 'done'. Once 'done' is entered, print out the largest and smallest
# of the numbers. If the user enters anything other than a valid number catch it
# with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

# Reference: https://www.py4e.com/html3/05-iterations


def checkMax(n):
    #print("max: ", n)
    if largest is None:
        return n
    elif largest < n:
        return n
    else:
        return largest


def checkMin(n):
    #print("min: ", n)
    if smallest is None:
        return n
    elif smallest > n:
        return n
    else:
        return smallest


largest = None
smallest = None

while True:
    num = input("Enter a number:")
    if num == "done" : break
    try:
        value = int(num)
    except:
        print("Invalid input")
        continue

    largest = checkMax(value)
    smallest = checkMin(value)


print("Maximum is", largest)
print("Minimum is", smallest)
