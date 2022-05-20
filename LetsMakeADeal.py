#Text based representation of the Monty Hall problem; Let's Make A Deal
import random
import time

#Allocating the prize door
def setup ():
    #random.seed("test_seed")
    doors = []

    i = 0
    while (i < 3):
        doors.append("Zonk!")
        i += 1
    
    randomDoor = random.randrange(0, 3)
    
    doors[randomDoor] = "Prize!"

    return doors

#User's first choice, between doors 1 and 3
def menu ():
    validChoice = False

    while (validChoice != True):
        print("Select your starting door! (1, 2, or 3)")
        choice = input()

        if (1 <= int(choice) <= 3):
            print("Your choice was door #%s!" % choice)
            print('*' * 30)
            validChoice = True
            return choice

        else:
            print("You must choose a valid door!")
            print('*' * 30)

#Will always reveal one wrong door
def reveal (choice):
    doors = setup()

    choice -= 1

    wrongDoor = random.randrange(0, 3)
    
    while (True):
        if (wrongDoor == choice or str(doors[wrongDoor]) == "Prize!"):
            wrongDoor = random.randrange(0, 3)
        else:
            break

    print("Revealing what's behind door #%s!" % (wrongDoor + 1))
    time.sleep(2)
    print("There is a Zonk behind door #%s!\n" % (wrongDoor + 1))

    #Creating a temporary list to determine the door to switch to
    newList = [0, 1, 2]

    newList.remove(choice)
    newList.remove(wrongDoor)
    #Last element in temp list
    newDoor = newList.pop()

    print("Would you like to switch to door #%s? (Y/N)" % (newDoor + 1))
    switch = str(input())

    while(True):
        if (switch.upper() != "Y" and switch.upper() != "N"):
            print("Would you like to switch to door #%s? (Y/N)" % (newDoor + 1))
            switch = input()
        else:
            if (switch.upper() == "Y"):
                break
            elif (switch.upper() == "N"):
                newDoor = choice
            break
    print('*' * 30)
    return newDoor, doors

def revealResults (choice, doors):
    print("Revealing what's behind door #%s...\nWhat's it going to be?\n" % (choice + 1))
    time.sleep(3)
    if (doors[choice] == "Prize!"):
        print("***Congratulations, you win!***")
    else:
        print("Better luck next time! The prize was in door #%s" % (doors.index("Prize!") + 1))
    
    print("The items behind the doors were: %s" % doors)

if __name__ == "__main__":
    choice = menu()
    newChoice, doors = reveal(int(choice))
    revealResults(newChoice, doors)