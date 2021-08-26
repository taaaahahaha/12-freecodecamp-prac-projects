# Taaha Multani @ https://github.com/taaaahahaha
# Words-list from https://www.randomlists.com/data/words.json

import random
from word import words

def valid_word(words):
    '''
    Since the word.py file contains words with spaces and -
    we need to filter out them.
    '''
    word = random.choice(words)
    while ' ' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    alphabets = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    word = valid_word(words).upper()
    word_letters = set(word)
    used_letters = set()
    lives = 10

    while len(word_letters)>0 and lives>0:
        # print(word_letters)

        print(f"You have {lives} lives left and you used these letters: "+(" ".join(used_letters)))

        # word_list = ['x' if letter in used_letters else '-' for letter in word]
        word_list = []
        for letter in word:
            if letter in used_letters:word_list.append(letter)
            else:word_list.append('-')
        # print(word_list)
        print("Current word:"+(' '.join(word_list)))

        cur_letter = input("Guess a letter: ").upper()

        if cur_letter in alphabets-used_letters:
            used_letters.add(cur_letter)
            if cur_letter in word_letters:
                word_letters.remove(cur_letter)
            else:
                lives-=1
                print("Letter not in the word.")
        elif cur_letter in used_letters:
            print("You have already used that character.")

        else:
            print("Invalid character.")
        
        print("")

    print(f"You died, word was {word}" if lives==0 else f"You guessed the word {word} !!")


if __name__ == '__main__':
    hangman()


