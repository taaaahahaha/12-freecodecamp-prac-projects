# Taaha Multani @ https://github.com/taaaahahaha

import random

def guess(x):
    rand_num = random.randint(1,x)
    guess = 0
    while guess!=rand_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess<rand_num:
            print("Sorry, guess again. Too low.")
        else:
            print("Sorry, guess again. Too high.")
    print(f"Congratulations, you have guessed the number {rand_num}")

if __name__=='__main__':
    guess(10)
    
