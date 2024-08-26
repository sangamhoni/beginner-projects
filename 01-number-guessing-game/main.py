import random

# my functions
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


# main program
lowerbound=input("Enter the lower bound: ")
upperbound=input("Enter the upper bound: ")

if (not is_int(upperbound) or not is_int(lowerbound)):
    print("Enter numbers as input")
    exit()

elif (upperbound<lowerbound):
    print("Upperbound is less than lowerbound")
    exit()

print("worked")






