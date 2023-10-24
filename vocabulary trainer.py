import random

#Delete and set your actual vocabulary here
vocabulary = {
    "Apple": "pomme",
    "Man": "homme",
    "Woman": "femme",
    "Car": "voiture",
    "Dog": "chien",
    "Cat": "chat",
    "Book": "livre",
    "Hello": "bonjour",
    "Goodbye": "au revoir"
}

while True:
  language1, language2 = random.choice(list(vocabulary.items()))
  #change to the correct language
  answer = input(f"What is the french word for \033[94m{language1}\033[0m?\n> ")
  if answer.lower() == language2.lower():
    print(f"\033[92mCorrect!\033[0m")
  else:
    print(f"\033[91mIncorrect!\033[0m\nThe correct answer is: \033[94m{language2}\033[0m.")
