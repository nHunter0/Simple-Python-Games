from time import sleep
import random
import os 

"""
    TODO: 
     - Verify type(user inputs ) == int 
"""

def new_file():
    print("---Welcome---")
    name = input("Please enter your name here: ")
    money = input("How much money are you gambling with today: ")
    game_data.write("-CASINO-GAME-DATA-" + "\n")
    game_data.write(str(name) + "\n")
    game_data.write(str(money) + "\n") 
    print("Hello, " + name)
    print("You have " + str(money) + "$ to play with")
    game_data.close()

def existing_file():
    print("---Welcome-Back---")
    game_data.readline() # Heading
    name = game_data.readline()
    money = game_data.readline()
    print("Welcome back, " + name + "You have " + str(money) + "$ to play with")
    game_data.close()

#File Handling 
if os.path.exists("game_data.txt"):
    game_data = open("game_data.txt","r+") 
    existing_file()
else:    
    open("game_data.txt", "a") #appending new file
    game_data = open("game_data.txt", "r+") 
    new_file()

def age_verification():
    user_age = int(input("Please input your age to continue: "))
    if user_age < 18: 
        playable_age = abs(18 - user_age) 
        print("Why are you gambling at age " + str(user_age) + "...") 
        print("Please leave and return when your 18 years of age in " + str(playable_age) + " years. Thank you")
        os.remove("game_data.txt")
        exit()
    if user_age > 18:
        pass

def obtain_data():
    game_data = open("game_data.txt")
    if os.path.exists("game_data.txt"):
        game_data.readline() # Heading
        name = game_data.readline()
        money = game_data.readline()
        return name, money
    else:    
        print("Problem with game_data file")
        exit()
 
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
        exit()

    while (playing == True):
        #Main Game
        
        play_money = int(input("Out of your " + str(money) + "$ how much would you like to gamble with:"))
        dice_roll = random.randint(1,6)

        if(play_money > int(money) or play_money == 0):
            print("Not enough money ??")
            print("I think its time for you to leave. BYE!")
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
            os.remove("game_data.txt")
            exit()

        #Continue playing 
        print("You now have : " + str(money) + "$")
        play_again = input("Would you like to continue to play ? (y/n): ")
        if(play_again == "y" or play_again == "Y"):
            os.system('cls')
            pass
        if(play_again == "n" or play_again == "N"):
            playing = False
            os.system("cls")
            print("---Results---")
            print("You stated with " + str(starting_money) + "$ and now have " + str(money) + "$")
           
            game_data.close()

            with open("game_data.txt","r") as f:
                data = f.readlines()

            str_money = str(money)
            data[2] = str_money

            with open("game_data.txt","w") as f:
                f.writelines(data)

            print("Thank you for playing!")
            exit()

#Main 
def run_casino():
    age_verification()
    name, money = obtain_data()
    play_game(money)

run_casino()
game_data.close()
