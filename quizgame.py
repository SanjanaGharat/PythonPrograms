#simple quiz game

print("welcome.....!!!!,Let's play a game")

name=input("Enter your name to continue: ")
score=0
print(name+"'s score= ",score) 
print("lets start")
print("Choose the subject to start")
print("1.COMPUTER")
print("2.MATHS")
print("3.CHEMISTRY")

sub=input()
if sub=="1":
    #code for computer quizz
    print("**use the option name whenever options are provided**")
    print("1ST QUESTION")
    print("What is software?")
    print("A.Clothing designed to be worn by computer users")
    print("B.Flexible parts of a computer case")
    print("C.Any part of the computer that has a physical structure")
    print("D.Instructions that tell the hardware what to do")
    answer=input("ENTER THE ANSWER: ")
    if answer.upper()!="D":
        print("Incorect....")
    else:
        print("That's correct")
        score+=1    
        print("score=",score)

    print("2nd QUESTION")
    print("The computer’s main circuit board is called a: ")
    ans2=input("ENTER UR ANSWER HERE: ")
    if ans2.lower()=="motherboard":
       print("That's correct")
       score+=1    
       print("score=",score) 
    else:
         print("Incorrect...")  
    
    print("3rd QUESTION")
    print("What does RAM stands for?")
    ans2=input("ENTER UR ANSWER HERE: ")
    if ans2.lower()=="random access memory":
         print("That's correct")
         score+=1    
         print("score=",score)
    else:
          print("Incorrect...")
                  
    print("4th QUESTION")
    print("What does 'GUI' stand for?")
    ans2=input("ENTER UR ANSWER HERE: ")
    if ans2.lower()=="graphical user interface":
        print("That's correct")
        score+=1    
        print("score=",score)
    else:
            print("Incorrect...")


    print("5th QUESTION")
    print("True or False: You cannot get a computer virus if you install antivirus software.")
    answer=input("ENTER THE ANSWER: ")
    if answer.lower()=="true":
      print("That's correct")
      score+=1    
      print("score=",score) 
        
    else:
          print("Incorect...")            
if score==0:
    print("oops...!!your score is ",score)
else:            
    print("congratulation.....Your score is ",score)

if sub=="2":
     #code for maths quizz
    print("1ST QUESTION")
    print("If David’s age is 27 years old in 2011. What was his age in 2003?")
    print("A.17")
    print("B.37")
    print("C.20")
    print("D.19")
    answer=input("ENTER THE ANSWER: ")
    if answer.upper()!="D":
        print("Incorect....")
    else:
        print("That's correct")
        score+=1    
        print("score=",score)
    print("2nd OUESTION")
    print("What is the remainder of 21 divided by 7?")  
    answer=int(input())
    if answer==0:
         print("That's correct")
         score+=1
         print("score=",score)
    else:
         print("Incorect...")     

    print("3RD QUESTION")
    print("I am a number. I have 7 in the ones place. I am less than 80 but greater than 70. What is my number?")
    print("A.71")
    print("B.73")
    print("C.75")
    print("D.77")
    answer=input("ENTER THE ANSWER: ")
    if answer.upper()!="D":
        print("Incorect....")
    else:
        print("That's correct")
        score+=1    
        print("score=",score)     

    print("4th OUESTION")
    print("What is the value of x if x2 = 169")  
    answer=int(input())
    if answer==13:
         print("That's correct")
         score+=1
         print("score=",score)
    else:
         print("Incorect...") 

    print("5th OUESTION")
    print("n a century how many months are there?")  
    answer=int(input())
    if answer==1200:
         print("That's correct")
         score+=1
         print("score=",score)
    else:
         print("Incorect...")        
if score==0:
    print("oops...!!your score is ",score)
else:            
    print("congratulation.....Your score is ",score)


if sub=="3":

     #code for chemistry quizz
    print("1ST QUESTION")
    print("If you fill a glass to the brim with ice water and the ice melts, what will happen?")
    print("A.The glass will over flow as the ice turns to water.")
    print("B.The level of water in the glass will remain unchanged as the ice melts.")
    print("C.The water level will drop slightly as the ice melts.")
    print("D.I'll never find out because I'll drink the water or walk away before anything happens.")
    answer=input("ENTER THE ANSWER: ")
    if answer.upper()!="c":
        print("Incorect....")
    else:
        print("That's correct")
        score+=1    
        print("score=",score)
    
    print("2nd QUESTION")
    print("Noble gases are inert because they have completed outer electron shells. Which of these elements isn't a noble gas?")
    print("A.Helium")
    print("B.Argon")
    print("C.Chlorine")
    print("D.Krypton")
    answer=input("ENTER THE ANSWER: ")
    if answer.upper()!="c":
        print("Incorect....")
    else:
        print("That's correct")
        score+=1    
        print("score=",score)
    print("3rd QUESTION")
    print("What is the most common isotope of hydrogen?")
    print("A.Protium")
    print("B.Deuterium")
    print("C.Tritum")
    print("D.Hydrogen only has one isotope!")
    answer=input("ENTER THE ANSWER: ")
    if answer.upper()!="A":
        print("Incorect....")
    else:
        print("That's correct")
        score+=1    
        print("score=",score)

    print("4th QUESTION")
    print("Who is credited with the invention of the modern periodic table?")
    print("A.Nobel")
    print("B.Lavoisier")
    print("C.mendel")
    print("D.mendeleev")
    answer=input("ENTER THE ANSWER: ")
    if answer.upper()!="D":
        print("Incorect....")
    else:
        print("That's correct")
        score+=1    
        print("score=",score)    
    print("5th QUESTION")
    print("Which of these elements is a nonmetal?")
    print("A.sulfur")
    print("B.Manganese")
    print("C.Aluminum")
    print("D.Beryllium")
    answer=input("ENTER THE ANSWER: ")
    if answer.upper()!="A":
        print("Incorect....")
    else:
        print("That's correct")
        score+=1    
if score==0:
    print("oops...!!your score is ",score)
else:            
    print("congratulation.....Your score is ",score)
