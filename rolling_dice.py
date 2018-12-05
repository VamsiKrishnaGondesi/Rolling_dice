#Python program to simple roll a random dice.

leave = 1
print("***DICE ROLLING***")
input("Press \"Enter\" to roll the dice")

#Loop to continuously roll a dice
#when there is 1,2,3,4,5,6.

while leave != "q":
    import random
    roll = random.randint(1, 6)
    #print a pattern that describes the number rolled on the dice
    if roll == 1:
        print("|----------|")
        print("|          |")
        print("|    O     |")
        print("|          |")
        print("|----------|")
        #variable to check for the exit or roll.
        leave = input("Press \"q\" to exit else press any key to roll")

    if roll == 2:
        print("|----------|")
        print("|          |")
        print("|  O    O  |")
        print("|          |")
        print("|----------|")
        leave = input("Press \"q\" to exit else press any key to roll")

    if roll == 3:
        print("|----------|")
        print("|  O   O   |")
        print("|    O     |")
        print("|          |")
        print("|----------|")
        leave = input("Press \"q\" to exit else press any key to roll")

    if roll == 4:
        print("|----------|")
        print("|  O    O  |")
        print("|          |")
        print("|  O    O  |")
        print("|----------|")
        leave = input("Press \"q\" to exit else press any key to roll")

    if roll == 5:
        print("|----------|")
        print("|  O   O   |")
        print("|    O     |")
        print("|  O   O   |")
        print("|----------|")
        leave = input("Press \"q\" to exit else press any key to roll")

    if roll == 6:
        print("|----------|")
        print("|  O   O   |")
        print("|  O   O   |")
        print("|  O   O   |")
        print("|----------|")
        leave = input("Press \"q\" to exit else press any key to roll")
 #end of program.
