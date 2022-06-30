from time import sleep
import random
import os 

"""
    TODO: 
     - Add game_data file to save users data after game conclusion
     - SPELL CHECK ! 
     - Verify type(user inputs ) == int 
"""

def age_verification():
    user_age = int(input("Please input your age to continue: "))
    if user_age < 18:
        playable_age = abs(18 - user_age) 
        print("Why are you gambling at age " + str(user_age) + "...") 
        print("Please leave and return when your 18 years of age in " + str(playable_age) + " years. Thank you")
        sleep(5)
        exit()
    if user_age > 18:
        pass

def obtain_data():
    name = input("Please enter your name here: ")
    money = input("How much money are you gambling with today: ")
    return name, money

def print_data(name, money):
    print("Hello, " + name)
    print("You have " + str(money) + "$ to play with")

def play_game(money):
    starting_money = money
    win = False
    playing = True
    print("--Game-Rules--")    
    print("A dice will role a number between 1 and 6, if you guess correct, double your money, if not well..")
    
    play = input("Would you like to continue and play? (y/n) ? ")
    if(play == "y"):
        pass
    if(play == "n"):
        playing = False
        print("Bye !")
        sleep(2)
        exit()

    while (playing == True):
        #Main Game
        play_money = int(input("Out of your " + money + "$ how much would you like to gamble with:"))
        dice_roll = random.randint(1,6)

        if(play_money > int(money) or play_money == 0):
            print("Not enough money ??")
            print("I think its time for you to leave. BYE!")
            sleep(5)
            exit()
        else:
            user_guess = int(input("Enter a number between 1 - 6: "))
            print("Dice rolled a..")
            sleep(1.5)
            print(dice_roll)
            
            if(dice_roll == user_guess ):
                won_money = play_money * 2 
                money = int(money) + won_money
                print("Wow congratulations! you have won " + str(won_money) + "$")
            else:
                print("Yikes you lost :(")
                money = int(money) - play_money
                print("You have lost " + str(play_money) + "$") 
        
        if(int(money) == 0 ):
            print("Dammmm looks like you have 0$")
            print("Thanks for the " + str(starting_money) + "$ and come back next time")
            #TODO: DELETE game_data file HERE !!
            sleep(5)
            exit()

        #Continue playing 
        print("You now have : " + str(money) + "$")
        play_again = input("Would you like to continue to play ? (y/n): ")
        if(play_again == "y" or play_again == "Y"):
            pass
        if(play_again == "n" or play_again == "N"):
            playing = False
            os.system("cls")
            print("---Results---")
            print("You stated with " + str(starting_money) + "$ and now have " + str(money) + "$")
            print("Thank you for playing!")
            sleep(5)
            exit()
        else: 
            print("invalid input")
            pass # if user_input =! 'y' or 'n' -> continue playing

#Main 
def run_casino():
    print("---Welcome---")
    age_verification()
    name, money = obtain_data()
    print_data(name, money)
    os.system("cls")
    play_game(money)


run_casino()