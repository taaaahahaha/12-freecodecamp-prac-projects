# Taaha Multani @ https://github.com/taaaahahaha

import random

def play():
    user = input("Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors. \n")
    computer = random.choice(['r','p','s'])

    if user==computer:return 'It\'s a tie'
    elif is_win(user,computer):
        return 'You won!'
    return 'You Lost!'




def is_win(p1,p2):
    '''
    True if Player wins(p1)
    '''
    if (p1 == 'r' and p2 == 's') or (p1 == 's' and p2 == 'p') or (p1 == 'p' and p2 == 'r'):
        return True

if __name__=='__main__':
    print(play())