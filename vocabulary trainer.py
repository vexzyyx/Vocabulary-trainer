import random

def colorize(text, color):
  colors = {
  'red': '\033[91m',
  'green': '\033[92m',
  'blue': '\033[94m'
   }
  return colors[color] + text + '\033[0m'

#set your vocabulary here
vocabulary = {"House":"Haus","Apple":"pomme","Man":"homme"}

while True:
  language1, language2 = random.choice(list(vocabulary.items()))
  #change to the correct language
  print("What is the --language-- word for " + colorize(language1, 'blue') + "?")
  answer = input("> ")
  if answer.lower() == language2.lower():
    print(colorize("Correct!", 'green'))
  else:
    print(colorize("Incorrect!", 'red'))
    print("The correct answer is: " + colorize(language2, 'blue'))
