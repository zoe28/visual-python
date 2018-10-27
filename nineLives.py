import random

lives = 9
words = ['pizza', 'family', 'teeth', 'otter', 'train', 'plane', 'earth']
secret_word = random.choice(words)
clue = list('??????') # store the clue
heart_symbol = u'\u2764' # show the lives left
guessed_word_correctly = False