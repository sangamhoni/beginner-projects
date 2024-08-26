# Number Guessing Game
Welcome to the Guessing Game! The goal is simple: guess a secret number chosen by the computer within a range you set. You’ll get hints if your guess is too high or too low. Guess it quickly to earn a "Congratulations!" or get a "Better Luck Next Time!" if you can't guess it within the set tries. Have fun and good luck!

&nbsp;  

## How to play
1. **Pick a range**: Enter the lowest and highest numbers you want to guess between.
2. The computer will **secretly choose** a number within that range.
3. **Start guessing!**
    - If you're **too high** or **too low**, don't worry—you'll get a hint to try again.
5. **Keep going** until you guess the right number!
6. If you guess it **quickly**, you'll get a "Congratulations!" If not, it's "Better Luck Next Time!"
Have fun, and see if you can outsmart the computer!

&nbsp;  

## Considerations and Features

#### Error Handling:
- Manages invalid inputs and prompts for correct data if non-numeric or out-of-range values are entered.
- Alerts user if lowerbound is not less than upperbound.

#### User Experience:
- Provides feedback: "Try Again! You guessed too high" or "Try Again! You guessed too small."
- Congratulates on correct guesses; otherwise, gives "Better Luck Next Time!" if guesses exceed the limit.

#### Edge Cases:
- Handles scenarios with no valid numbers between bounds and ensures bounds are valid.

#### Input Validation:
- Ensures inputs are integers and within the valid range, guiding users to provide correct values.
