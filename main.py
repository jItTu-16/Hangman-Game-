import random
import os
import time
from words import words
from words import alphabets
from hangman_visual import chances_visual


def get_word(words):
    word = random.choice(words)
    return word.upper()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def user_input():
    user_letter = input("Guess a letter : ").upper()
    return user_letter


def check(user_letter,used_letters,word_letter,chances):
    if user_letter in alphabets - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letter:
            word_letter.remove(user_letter)
            print('')
        else:
            chances-=1
            print('\nYour letter,', user_letter, 'is not in the word.')

    elif user_letter in used_letters:
        print("You have already used that letter. Please try again.")

    else:
        print("Invalid character. Please try again.")

    return chances

def hangman():
    while True:
        clear_screen()
        word = get_word(words)
        word_letter = set(word)
        used_letters = set()

        chances = 7

        while len(word_letter) > 0 and chances > 0:
            time.sleep(0.5)

            print(f'You have {chances} lives left and you have used these letters: {' '.join(used_letters)}')

            word_list = [letter if letter in used_letters else '_' for letter in word]
            print(chances_visual[chances])
            print('Current word: ', ' '.join(word_list))

            user_letter = user_input()
            chances = check(user_letter,used_letters,word_letter,chances)

        clear_screen()
        if chances == 0:
            print(chances_visual[chances])
            print(f"The player is DEAD!!!. The word was {word}")
        else:
            print(f"Congratulation!!!, You guessed the word {word} !!")
            print(chances_visual[9])

        play_again = input("\nDo you want to play again? (Y/N): ").strip().upper()
        if play_again != 'Y':
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    hangman()
