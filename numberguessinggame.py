#THE SIMPLE GAME TO GUESS THE RANDOM NUMBERS
import random
number1 = random.randint(0,10)
number2= random.randint(0,50)
number3= random.randint(0,100)

Guess=0
guess=0

print("LET'S PLAY NUMBER GUESSING GAME")
print("SELECT THE LEVEL TO START")
print("level1")
print("level2")
print("level3")

level=input()

if level=="level1":
    print("HINT:THE NUMBER IS BETWEEN 0-10")
    while guess!=number1:
        Guess+=1
        guess=int(input("Enter Guess:"))

        if(guess<number1):
            print("Guess higher!")
        elif(guess>number1):
            print("Guess lower!")
        else:
            print("You Won...!!")        
    print("You got that in ",Guess,"guesses")

if level=="level2":
    print("HINT:THE NUMBER IS BETWEEN 0-50")
    while guess!=number2:
        Guess+=1
        guess=int(input("Enter Guess:"))

        if(guess<number2):
            print("Guess higher!")
        elif(guess>number2):
            print("Guess lower!")
        else:
            print("You Won...!!")        
    print("You got that in ",Guess,"guesses") 

if level=="level3":
    print("HINT:THE NUMBER IS BETWEEN 0-100")
    while guess!=number3:
        Guess+=1
        guess=int(input("Enter Guess:"))

        if(guess<number3):
            print("Guess higher!")
        elif(guess>number3):
            print("Guess lower!")
        else:
            print("You Won...!!")        
    print("You got that in ",Guess,"guesses")      