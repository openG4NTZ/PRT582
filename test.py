import unittest
from hangman import Hangman
from EnglishWords import English_Words
#Boundary conditions or Edge Cases
class HangmanTestCases(unittest.TestCase):
    #Test Case 1
    def test_English_Word_Database(self):
        # Capture the results from the function
        result=English_Words.get_English_Word(111)
        # Check for expected output
        expected="abusive"
        self.assertEqual(expected,result,msg="Test Case 1 Fail")
    #Test Case 2
    def test_random_Word_Generator(self):
        # Capture the results from the function
        newWord=Hangman.random_Word_Generator(1)
        if newWord in list(English_Words.set):
           result=True
        else:
           result=False
        # Check for expected output
        expected=True
        self.assertEqual(expected,result)
    #Test Case 3
    def test_split_Word(self):
        # Capture the results from the function
        result=English_Words.get_English_Word(111)
        # Check for expected output
        expected="abusive"
        self.assertEqual(expected,result)
# Run the test
if __name__ == '__main__':
    unittest.main()
