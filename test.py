import unittest
import io
from io import StringIO
from unittest.mock import patch
from hangman import Hangman
from EnglishWords import English_Words
#Boundary conditions or Edge Cases
class HangmanTestCases(unittest.TestCase):
    #Test Case 1: Check English Database
    def test_English_Word_Database(self):
        # Capture the results from the function
        result=English_Words.get_English_Word(7825)
        # Check for expected output
        expected="english"
        self.assertEqual(expected,result,msg="Test Case 1 Failed")
    #Test Case 2: Check Random Word Generetor
    def test_random_Word_Generator(self):
        RandomWord=Hangman.random_Word_Generator(self)
        self.assertTrue((RandomWord in list(English_Words.set)),msg="Test Case 2 Failed")
    #Test Case 3: Check function for splitting words
    def test_split_Word(self):
        result=Hangman.split_Word(self,"serkan")
        expected=['s','e','r','k','a','n']
        self.assertEqual(expected,result,msg="Test Case 3 Failed")
    #Test Case 4: Check game dificulty and coreresponding amount of life
    def test_lifecalculator(self):
        # Capture the results from the function
        if Hangman.lifecalculator(self,'1')==8 and Hangman.lifecalculator(self,'2')==6 and Hangman.lifecalculator(self,'3')==3:
            result=True
        else:
            result=False
        # Check for expected output
        expected=True
        self.assertEqual(expected,result,msg="Test Case 4 Failed")
    #Test Case 5: Test possible error messages
    def test_print_Error1(self):
        # Capture the results from the function
        result=Hangman.print_Error(self,"Wrong_User_Input")
        # Check for expected output
        expected="Wrong keyboard entry... "
        self.assertEqual(expected,result,msg="Test Case 5 Failed")
    #Test Case 6: Test possible error messages
    def test_print_Error2(self):
        # Capture the results from the function
        result=Hangman.print_Error(self,"SameLetter")
        # Check for expected output
        expected="This letter has already been found..."
        self.assertEqual(expected,result,msg="Test Case 6 Failed")
        # get_input will return 'yes' during this test
    #Test Case 7: Test User Interface
    @patch('builtins.input', side_effect=['1', '2', '3', '4'])
    #this function simulates user inputs,
    def test_user_GUI(self, mock_input):
        #function user_GUI called 4 times with '1', '2', '3', '4' inputs
        calling_1 = Hangman.user_GUI(self,"Intro",0)
        calling_2 = Hangman.user_GUI(self,"Intro",0)
        calling_3 = Hangman.user_GUI(self,"Intro",0)
        calling_4 = Hangman.user_GUI(self,"Intro",0)
        # Check for expected output
        self.assertTrue(calling_1 == '1' and calling_2 == '2' and
                        calling_3 == '3' and calling_4 == '4',msg="Test Case 7 Failed")
    #Test Case 8: Test correct guess
    @patch('builtins.input', side_effect=['s', 'e', 'r', 'k', 'a', 'n'])
    def test_start_Game1(self,mock_input):
        # Capture the results from the function
        test_Game =Hangman()
        result=test_Game.start_Game("serkan",8)
        # Check for expected output
        expected=True
        self.assertEqual(expected,result,msg="Test Case 8 Failed")
        # get_input will return 'yes' during this test#Test Case 8: Test actual game
    #Test Case 9: Test wrong guess
    @patch('builtins.input', side_effect=['b', 'c', 'd'])
    def test_start_Game2(self,mock_input):
        # Capture the results from the function
        test_Game =Hangman()
        result=test_Game.start_Game("serkan",3)
        # Check for expected output
        expected=False
        self.assertEqual(expected,result,msg="Test Case 9 Failed")
        # get_input will return 'yes' during this test
# Run the test
if __name__ == '__main__':
    unittest.main()
