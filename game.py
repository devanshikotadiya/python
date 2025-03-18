import random
target=random.randint(1,100)

while True:
    userchoice=input("Guess the target or quit:")
    if(userchoice=="Quit"):
        break

    userchoice=int(userchoice)
    if(userchoice==target):
        print("success:correct guess!!")
        break
    elif(userchoice<target):
        print("your number was to small take a bigger guess...")
    else:
        print("your number was to big take a smaller guess...")

print("..................Game over........................")    