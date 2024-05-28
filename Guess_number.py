import random
number= random.randint(1,10)
guess=int(input("Enter the number between 1 to 10:"))
while guess!= number:
  if guess < number:
    print("Your Guess is Low!")
  elif guess > number:
    print("Your guess is High!")
  print("You loss!")
  print(int(input("guess again:")))
print("You won!")
print("Your guess is right!")
