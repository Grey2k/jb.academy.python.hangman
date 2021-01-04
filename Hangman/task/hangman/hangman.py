# Write your code here
GAME = 'hangman'
WORD = 'python'

print(' '.join([ch.upper() for ch in list(GAME)]))

word = input('Guess the word: ')

print('You survived!' if word == WORD else 'You lost!')
