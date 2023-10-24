import random

#set your vocabulary here
vocabulary = {"House":"Haus","Apple":"pomme","Man":"homme"}

while True:
  language1, language2 = random.choice(list(vocabulary.items()))
  #change to the correct language
  answer = input(f"What is the --language-- word for \033[94m{language1}\033[0m?\n> ")
  if answer.lower() == language2.lower():
    print(f"\033[92mCorrect!\033[0m")
  else:
    print(f"\033[91mIncorrect!\033[0m\nThe correct answer is: \033[94m{language2}\033[0m.")
