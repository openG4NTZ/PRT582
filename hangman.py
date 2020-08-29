import random
import string
import sys
from EnglishWords import English_Words
class Hangman:
    # Generates random number between the numbers 0 and 25480
    #English_Words class has 254800 words and it captures one word
    # Where the index number is equel to random number
    def random_Word_Generator(Self):
        global random
        random=random.randint(0,25480)
        return English_Words.get_English_Word(random)
    #Splits Strings to list
    def split_Word(Self,Word):
        return list(Word)
    #Calculates number of lifes depends on lvl of difficulty
    def lifecalculator(Self,Difficultylevel):
        if Difficultylevel=='1':
            return 8
        elif Difficultylevel=='2':
            return 6
        elif Difficultylevel=='3':
            return 3
        elif Difficultylevel=='4':
            # if user chooses number 4 game closes
            Self.end_Game()
        else:
            # if user enters anyother number it go calls back the same function recursively
            return Self.lifecalculator(Self.user_GUI("Intro",0))
    # It returns error outputs depending on error codes
    def print_Error(Self,ErrorCode):
        if ErrorCode == "WrongLetter":
           # Wrong keyboard entry such as double letter, number or special char
           return "Wrong keyboard entry... "
        elif ErrorCode == "SameLetter":
           # If user enters the visiable letters again this msgg shows
           return "This letter has already been found..."
    # This function returns user inputs depending on game status
    def user_GUI(Self,GameStatus,NumberofLife):
        global ScreenGap
        ScreenGap="""                     """
        # beginning of the game
        if GameStatus == "Intro":
           return input("""
                     Welcome to Hangman Game

                     Please choose a difficulty level to start the game:
                     1. Easy (8 Misses)
                     2. Medium (6 Misses)
                     3. Advanced (3 Misses)
                     4. Exit Game
                     """)
        elif GameStatus == "Starting":
        # first User entry
            return input(ScreenGap+"Hangman is starting, number of lives: "+str(NumberofLife)+"\n" + ScreenGap+"Please enter a single letter\n")
        elif GameStatus == "Started":
        # second and later entries
           if NumberofLife > 0:
               return input (ScreenGap+"Please enter a single letter\n")
           else:
               # out of life
               print(ScreenGap+"GAME OVER...")
               return True
    # Starts the game and does necesary calculations
    def start_Game(Self):
        # Calculates numberoflife depends on difficulty chosen by user
        NumberofLife=Self.lifecalculator(Self.user_GUI("Intro",0))
        #Random wordd Generated
        random_Word=Self.random_Word_Generator()
        splitted_random_Word=Self.split_Word(random_Word)
        Random_Word_Hidden=Self.split_Word(random_Word)
        # Random_Word_Hidden holds users correct guesses
        # it is also used for understanding user progress
        for x in range(len(Random_Word_Hidden)):
            Random_Word_Hidden[x]="_"
        user_input=Self.user_GUI("Starting",NumberofLife)
        # While loop used for to get multiple entries from user
        # it is also dynamicly handles different type of entries
        while NumberofLife > 0:
            #Checks if user input is not a single letter
            if user_input not in list(string.ascii_letters):
                print(ScreenGap+Self.print_Error("WrongLetter"))
            # compares user input with actual word
            elif user_input not in list(splitted_random_Word):
                NumberofLife-=1
                print(ScreenGap+"Wrong Entry")
            # if it is a correct guess there us two possibility
            else:
                for x in range(len(splitted_random_Word)):
                    # 1. new cirrect guess
                    if splitted_random_Word[x]==user_input and  Random_Word_Hidden[x]!=user_input:
                        Random_Word_Hidden[x]=user_input
                    # 2. old correct guess
                    elif Random_Word_Hidden[x]==user_input:
                        print(ScreenGap+Self.print_Error("SameLetter"))
                        break
            # puts all items together and shows to user his progress
            print(ScreenGap+' '.join(Random_Word_Hidden))
            # shows reamaing lives to user
            print(ScreenGap+"Remaing lives: ",NumberofLife)
            # if there is no empty space in Random_Word_Hidden that means user guess everything
            if "_" not in list(Random_Word_Hidden):
                print(ScreenGap+"Congratulation... YOU WON....")
                break
            # End of user input control, new input requested
            user_input=Self.user_GUI("Started",NumberofLife)
        print(ScreenGap+"The hidden word :" + random_Word)
    # It closes the game
    def end_Game(Self):
        sys.exit(0)
