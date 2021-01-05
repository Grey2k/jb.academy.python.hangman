import random
import string

# Write your code here
GAME = 'hangman'
LIVES = 8
DICTIONARY = ['python', 'java', 'kotlin', 'javascript']

print(' '.join([ch.upper() for ch in list(GAME)]))

while True:
    command = input('Type "play" to play the game, "exit" to quit: ')
    if command == 'play':
        break

    if command == 'exit':
        exit(0)


def generate_word():
    return random.choice(DICTIONARY)


def get_hint(secret: str, hints: set) -> str:
    result = []
    for i, char in enumerate(secret):
        if char in hints:
            result.append(char)
        else:
            result.append('-')

    return ''.join(result)


########

word = generate_word()
lives = LIVES

found = set()
guessed = set()
word_set = set(word)

while True:
    if lives <= 0:
        break

    print("\n{hint}".format(hint=get_hint(word, found)))
    letter = input('Input a letter: ')

    if len(letter) != 1:
        print('You should input a single letter')
        continue

    if letter not in string.ascii_lowercase:
        print('Please enter a lowercase English letter')
        continue

    if letter in guessed:
        print("You've already guessed this letter")
        continue

    guessed.add(letter)

    if letter not in word_set:
        print("That letter doesn't appear in the word")
        lives -= 1
        continue

    found.add(letter)

    if found == word_set:
        print(word)
        print("You guessed the word!")
        break

# END
if lives > 0:
    print("You survived!")
else:
    print('You lost!')
