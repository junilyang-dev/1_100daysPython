print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person.")
print("color", "\033[31m", "red", "\033[30m", "black",
      "\033[32m", "green",
      "\033[33m", "yellow",
      "\033[34m", "blue",
      "\033[35m", "purple",
      "\033[36m", "cyan",
      "\033[37m", "white",
      "\033[0m", "default")
print("Welcome to your Adventure Story Simulator.")
print ()
print("I am going to ask you a bunch of questions and then create an epic story with you as the star.")

print()
name = input("What is your name? ")
print()
enemyName = input("What is your enemy's name? ")
print()
superPower = input("What is your super power? ")
print()
live = input("Where do you live?")
print()
food = input("What is your favorite food?")

print()
print("Hello", name, "Your ability to", superPower, "will make sure you never have to look at", enemyName, "again." "Go eat", food, "as you walk down the streets of", live, "and use", superPower, "for good and not evil!")