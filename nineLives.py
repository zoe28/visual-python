import random

lives = 9
words = ['pizza', 'family', 'teeth', 'otter', 'train', 'plane', 'earth', 'light', 'brush']
secret_word = random.choice(words)
clue = list('??????') # store the clue
heart_symbol = u'\u2764' # show the lives left
guessed_word_correctly = False 
# The variable is set as False to begin with because the player doesn't know the word when the game starts

def update_clue(guessed_letter, secret_word, clue, unknown_letters):
  index = 0
  while index < len(secret_word):

    if guessed_letter == secret_word[index]:
      clue[index] = guessed_letter
      unknown_letters = unknown_letters - 1
    index = index + 1

  return unknown_letters

difficulty = input('Choose difficulty (type 1, 2 or 3):\n 1 Easy\n 2 Normal\n 3 Hard\n')
difficulty = int(difficulty)

if difficulty == 1:
  lives = 12
elif difficulty == 2:
  lives = 9
else:
  lives = 6

clue = []
index = []
while index < len(secret_word):
  clue.append('?')
  index = index + 1

while lives > 0:
  print(clue)
  print('Lives left: ' + heart_symbol * lives)
  guess = input('Guess a letter or the whole word: ')

  if guess == secret_word:
    guessed_word_correctly = True
    break

  if guess in secret_word:
    unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
  else:
    print('Incorrect. You lose a life')
    lives = lives - 1

  if unknown_letters == 0:
    guessed_word_correctly = True
    break

#if guessed_word_correctly:
  #print('You won! The secret word was ' + secret_word)
#else:
  #print('You lost! The secret word was ' + secret_word)
