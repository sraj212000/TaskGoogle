import random as r
s1=["Snake","Water","Gun"]


while True:
    choi=input("Enter your choice Snake , Gun , Water and Quit to exit : ")
    if (choi!="Quit"):
        computer=r.choice(s1)
        print(f"your choice is {choi} and Computer's choice is {computer}")
    else:
        break
    if(computer==choi):
        print("Match Draw")
    elif(choi=='Snake' and computer=='Water'):
        print("you won")
    elif(choi=='Snake'and computer=='Gun'):
        print("you Lost")
    elif(choi=='Water'and computer=='Gun'):
        print("you Won")
    elif(choi=='Water'and computer=='Snake'):
        print("you Lost")
    elif(choi=='Gun'and computer=='Snake'):
        print("you Won")
    elif(choi=='Gun'and computer=='Water'):
        print("you Lost")
    else:
        print("Wrong Choice")




