import random

lives = 9
words = ['pizza', 'family', 'teeth', 'otter', 'train', 'plane', 'earth']
secret_word = random.choice(words)
clue = list('??????') # store the clue
heart_symbol = u'\u2764' # show the lives left
guessed_word_correctly = False 
# The variable is set as False to begin with because the player doesn't know the word when the game starts

def update_clue(guessed_letter, secret_word, clue):
  index = 0
  while index < len(secret_word):

    if guessed_letter == secret_word[index]:
      clue[index] = guessed_letter
    index = index + 1

while lives > 0:
  print(clue)
  print('Lives left: ' + heart_symbol * lives)
  guess = input('Guess a letter or the whole word: ')

  if guess == secret_word:
    guessed_word_correctly = True
    break

  if guess in secret_word:
    update_clue(guess, secret_word, clue)
  else:
    print('Incorrect. You lose a life')
    lives = lives - 1
