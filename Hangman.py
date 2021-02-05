import random
import string
from word import words


def get_valid_word(words):
    word = random.choice(words)  # randomly choose a word from list
    while '-' in word or ' ' in word:  # if - or space in between word select another word
        word = random.choice(words)  # Select another word
    return word.upper()


def hangman():
    word = get_valid_word(words)  # Getting Valid words #DISAGREE
    word_letters = set(word)  # {'G', 'D', 'I', 'A', 'S', 'E', 'R'}
    alphabet = set(string.ascii_uppercase)  # 26 Letters
    used_letters = set()  # what user has guessed
    lives = 6
    while len(word_letters) > 0 and lives > 0:  # Till all the letter are guess
        # Letters used
        # ' '.join(['a','b','cd'] --> 'a b cd'
        print('You have', lives, 'lives left and used these letter:',
              ' '.join(used_letters))
        # What current word is (W - R D)
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        # Getting User input
        user_letter = input('Guess a letter:').upper()
        # 1 Condition
        # User letter in alphabet and then that alphabet is not in used letter add it
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            # 2 Condition
            # Remove letter from word letter
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives-1
                print('Letter is not in word ')

        elif user_letter in used_letters:
            print('You have already used that letter.Please try again')
        else:
            print('Invalid Charater.Please try again')
    # Get when length of  word_letter==0 OR when lives ==0
    if lives == 0:
        print('You have died')

    print('You have guess the correct word', word, '!!')


hangman()
