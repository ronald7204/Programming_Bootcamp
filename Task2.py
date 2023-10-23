"""
input: user guess
output: higher or lower or correct

requirements: 
- check for valid inputs 
"""

import re

#things to do
#validate user input
#generate target number
#allow user to guess 
#compare guess with target number
def valid_input():
    guess = input()
    if re.search(r"\d+", guess):
        guess = int(guess)
        if guess > 1 and guess < 100:
            print("yay") #assuming that 1 and 100 are not included since "between"
            return guess
        else: 
            print("please input an integer between 1 and 100")
            return valid_input()
    else: 
        print("please input an integer")
        return valid_input()
    


"""running code & testcases"""
valid_input()
