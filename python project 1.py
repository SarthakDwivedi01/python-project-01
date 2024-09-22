print("HELLO! THIS IS SARTHAK")
print("Welcome To My Computer Quiz!!")
a=input("enter your name")
print(a)
playing=input("do you want to play? ")
if (playing !="yes"):
    quit()
print("okay let's play :)")
score=0

answer=input("what is the full form of CPU?")
if answer.lower()=="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("what does GPU stands for?")
if answer.lower()=="graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("what does RAM stands for?")
if answer.lower()=="random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("who is known as the Father of Computer?")
if answer.lower()=="charles baggage":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("what is the full form of e-mail?")
if answer.lower()=="electronic mail":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("You got "+ str(score) + " questions correct out of 5")
print("You got " + str(score/5*100)+ " %")






