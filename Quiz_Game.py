print("Welcome to Quiz Game!!")
player=input("Do you want to play?")
if player != "yes":
  quit()
print("Game Starts!!!")
score=0
question=input("which part is known as memory unit in computer?")
if question.lower()=="cpu":
  print("Correct!!")
  score=+5
else:
  print("Incorrect!!")
question=input("how many vowels are in alphabets?")
if question.lower()=="six":
  print("Correct!")
  score=+5
else:
  print("Incorrect")
question=input("what is the SI unit for energy?")
if question.lower()=="joule":
  print("Correct!")
  score=+5
else:
  print("Incorrect!")
question=input("what is the pigment present in the plants?")
if question.lower()=="chloropyll":
  print("Correct!")
  score=+5
else:
  print("incorrect!")
question=input("what is known as powerhouse of cells?")
if question.lower()=="mitochondria":
  print("Correct!")
  score+=5
else:
  print("Incorrect!")
print("Your Total Score is" +str(score))
