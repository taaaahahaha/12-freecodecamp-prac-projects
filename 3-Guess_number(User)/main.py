# Taaha Multani @ https://github.com/taaaahahaha

import random

def comp_guess(x):
    low,high = 1,x
    feedback = ''
    while feedback != 'c' and low != high:
        if low != high:
            guess = random.randint(low,high)
        # else:
        #     guess = low #Could be high since low==high
        feedback = input(f"Is {guess} too high (H), too low (L), or correct.(C)").lower()
        if feedback=='h':
            high = guess-1
        else:
            low = guess+1
    print(f"Yay! The computer guessed the number, {guess}, correctly.")

if __name__ == '__main__':
    print("Think of number between 1 and 1000.")
    comp_guess(1000)
