import random

# Write your code here
GAME = 'hangman'
LIVES = 8
DICTIONARY = ['python', 'java', 'kotlin', 'javascript']

print(' '.join([ch.upper() for ch in list(GAME)]))


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
letters = set()
word_set = set(word)

while True:
    if lives <= 0:
        break

    print("\n{hint}".format(hint=get_hint(word, letters)))
    letter = input('Input a letter: ')

    if letter not in word_set:
        print("That letter doesn't appear in the word")
        lives -= 1
        continue

    if letter in letters:
        print('No improvements')
        lives -= 1
        continue

    letters.add(letter)

    if letters == word_set:
        print(word)
        print("You guessed the word!")
        break

# END
if lives > 0:
    print("You survived!")
else:
    print('You lost!')
