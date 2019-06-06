# game_test.py

from game import my_message, determine_winner #use this to reach into game file and pull function from it.
#it imports all code from the global scope - indented left - function. so we have to 
#use convent if __name__ == "__main__":
    #pass

def test_example():
    assert 2 == 2

def test_my_message():
    x = my_message()
    assert x == "HELLO"

#
#function name must begin with test_ in order to be recongized as a test

#Example
#from game import determine_winner
#
def test_determination_of_the_winner():
    assert determine_winner("rock", "rock") == None # represents a tie
    assert determine_winner("rock", "paper") == "paper"
    assert determine_winner("rock", "scissors") == "rock"

    assert determine_winner("paper", "rock") == "paper"
    assert determine_winner("paper", "paper") == None # represents a tie
    assert determine_winner("paper", "scissors") == "scissors"

    assert determine_winner("scissors", "rock") == "rock"
    assert determine_winner("scissors", "paper") == "scissors"
    assert determine_winner("scissors", "scissors") == None # represents a tie