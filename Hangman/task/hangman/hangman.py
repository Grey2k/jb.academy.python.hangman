import random

# Write your code here
GAME = 'hangman'

print(' '.join([ch.upper() for ch in list(GAME)]))


def generate_word():
    return random.choice(['python', 'java', 'kotlin', 'javascript'])


word = generate_word()
answer = input('Guess the word: ')

print('You survived!' if answer == word else 'You lost!')
