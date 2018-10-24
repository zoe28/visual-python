import random
import string

adjectives = ['sleepy', 'happy', 'slow', 'sad', 'wet', 'strong', 'fat', 'yellow', 'fluffy', 'white', 'pround', 'brave']
nouns = ['apple', 'name', 'coffee', 'San Franciso', 'wine', 'hammer', 'panada', 'Holiday', 'toaster']

print('Welcome to Password Picker!')

while True:
  adjectives = random.choice(adjectives)
  nouns = random.choice(nouns)
  number = random.randrange(0, 100)
  special_char = random.choice(string.punctuation)

  password = adjectives + nouns + str(number) + special_char
  print('Your new password is : %s' % password)
