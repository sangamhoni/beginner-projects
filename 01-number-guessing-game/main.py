import math
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

upperbound=int(upperbound)
lowerbound=int(lowerbound)  

if (upperbound<lowerbound):
    print("Invalid range. Upperbound is less than lowerbound.")
    exit()
elif (upperbound-lowerbound<3):
    print("Range too small to guess.")
    exit()

total_guess=math.log2((upperbound-1)-(lowerbound+1)+1)//1
answer=random.randint(lowerbound+1, upperbound-1)

print(f"\nYou have {int(total_guess)} tries to guess a number between {lowerbound} and {upperbound}.")

guess_count=0

while (guess_count!=total_guess):
    guess=input("Guess a number: ")
    # error handling for invalid input
    if (not is_int(guess)):
        print("Input should be an integer.")
        exit()
    
    guess=int(guess)
    guess_count=guess_count+1
    
    if (guess != answer):
        if (guess > answer):
            print("You guessed too high.")
        else:
            print("You guessed too small")
    else:
        print(f"Congratulations! You guessed it in {guess_count} tries.")
        exit()
        
print(f"\nThe number was {answer}. Better Luck Next Time!")
