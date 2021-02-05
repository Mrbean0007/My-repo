import random


def play():
    user = input('r for rock, s for scissor, p for paper:')
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return 'You won'

    return 'You loss'


def is_win(user, opponents):
    if (user == 'r' and opponents == 's') or (user == 's' and opponents == 'p') \
            or (user == 'p' and opponents == 'r'):
        return True


print(play())
