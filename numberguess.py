import random

Num= random.randint(1,10)
for i in range(0,4):
    UserInput=int(input("Guess a number from 1 to 10: "))
    if(UserInput>Num):
      print("Too high, try guessing lower")
    elif(UserInput<Num):
      print("Too low, try guessing higher")
    else:
      print("Congrats you have guessed right number!!")        

if(UserInput==Num):
   print("Bye Job well done")
else:
   print("You ended your four trials...better luck next time!!")   