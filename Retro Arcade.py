#Sarah Opalenik
#Project 2
#11/8/18

import random



#######################

#######################

#game start
def gamestart():
    name = input("Welcome to Retro Arcade! Please enter your name:")
    print("Welcome, " + name + " !")
    print("Your game options are:")
    options = ["Dice", "Slots", "Madlib", "Quit"]
    print(options)
    game = input("Please enter 'D' for Dice, 'S' for Slots, 'M' for Madlib, or 'Q' for Quit:")
    if game == "D":
        def dice():
        #Dice Game:
            result1 = random.randint(1,6)
            result2 = random.randint(1,6)
            print(name + " rolled", + result1)
            print("Computer rolled", + result2)
            if result1 > result2:
                print(name + " wins!")
            elif result1 < result2:
                print("Computer wins!")
            else:
                print("You tied, Computer wins!")
            
        dice()
        
        done = False
        while done == False:
            PA = input("Play again?")
            if PA == "no":
                done = True
                print("Thanks for playing!"
                #need to prompt here to choose another game
                #break
            #elif PA == "yes":
            elif PA == "yes":
                dice()
            else:
                print("Please enter 'yes' or 'no'")
    if game == "S":
        #slotItems = ["grapes", "cherries", "apple", "banana", "orange"]
        slotItems = ["apples"]
        slot1 = random.choice(slotItems)
        slot2 = random.choice(slotItems)
        slot3 = random.choice(slotItems)
        def slots():
            print(slot1)
            print(slot2)
            print(slot3)
            if slot1 == slot2 and slot2 == slot3:
                print(name + " wins!")
            elif slot1 != slot2 and slot2 != slot3:
                print("Computer wins!")
           
        slots()
        
        done = False
        while done == False:
            PA = input("Play again?")
            if PA == "no":
                done = True
                print("Thanks for playing!")
                #need to prompt here to choose another game
                #break
            elif PA == "yes":
                slots()
            else:
                print("Please enter 'yes' or 'no'")
    if game == "M":
        #madlib()
        def generateMadlib():
            ADJ_LIST = ["normal", "fun", "intelligent", "regular", "friendly", "automated", ]
            NOUN_LIST = ["human", "robot", "computer", "bot", "friend", "user"]
            ADVERB_LIST = ["efficiently", "carefully", "maliciously", "successfully"]
            INTERJ_LIST = ["Beep Boop!", "Yeah!", "Congratulations!", "Vroom!", "Wow!"]

            # Setup the output string that will contain the Madlib
            output = ""

            # Step 2. Write your Madlib below using String concatenation and the random.choice() function
            output += "Hello, I'm just a " + random.choice(ADJ_LIST) + " " + random.choice(NOUN_LIST) + "! " + random.choice(INTERJ_LIST) + " Not a " + random.choice(NOUN_LIST)
            output += "! Yesterday, a " + random.choice(NOUN_LIST) + " " + random.choice(ADVERB_LIST) + " made a Madlib in python! " + random.choice(INTERJ_LIST) + " "
            output += "Did you know you can " + random.choice(ADVERB_LIST) + " pretend to be a " + random.choice(ADJ_LIST) + " " + random.choice(NOUN_LIST) + " when you " + random.choice(ADVERB_LIST) + " choose your words?"
            output += " Spooky Stuff! I hope you " + random.choice(ADVERB_LIST) + " have a " + random.choice(ADJ_LIST) + " day! " + random.choice(INTERJ_LIST)                 


            # Return generated Madlib
            return output

        #here I use a while loop to let the user decide if they want to keep generating
        #new madlibs. 

            madlib=generateMadlib()

            print(madlib)

        #madlib = generateMadlib()
        done = False

        while done == False:
            PA = input("Play again?")
            if PA == "no":
                done = True
                print("Thanks for playing!")
                break
            elif PA == "yes":
                madlib = generateMadlib()
                print(madlib)
            else:
                print("Please enter 'yes' or 'no'")
    if game == "Q":
                print("Thanks for playing," + name + "! See you next time!")

    

#######################
gamestart()

#Still have to:
#
#
#
