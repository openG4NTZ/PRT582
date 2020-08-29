from hangman import Hangman
# New class defined
newGame= Hangman()
#Infinite loop to start the  game continuously.
while True:
    # Calculates numberoflife depends on difficulty chosen by user
    NumberofLife=newGame.lifecalculator(newGame.user_GUI("Intro",0))
    #Random wordd Generated
    random_Word=newGame.random_Word_Generator()
    newGame.start_Game(random_Word,NumberofLife)
