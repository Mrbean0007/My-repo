import random


def guess(x):
    random_no = random.randint(1, x)
    guess = 0
    while guess != random_no:
        guess = int(input(f'Guess a number between 1 and {x}:'))
        if guess < random_no:
            print('To low, Guess again')
        if guess > random_no:
            print('To High, Guess again')
    print(f'Congrats You guess the right no {random_no}')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(
            f'Is {guess} too High (H) or too Low (L) or Correct (C):').lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
    print(f'Yay! Computer guess your number correct {guess} ')


computer_guess(10)
