"""
input: user guess
output: higher or lower or correct

requirements: 
- check for valid inputs 
"""

import re
from random import randint

def generate_number():
    target = randint(1, 100)
    return target


def validate_input(target:int):
    guess = input("Please enter an integer between [1,100]: ")
    if re.search(r"\d+", guess):
        guess = int(guess)
        if guess >= 1 and guess <= 100:
            # print("yay") #assuming that 1 and 100 are not included since "between"
            # return guess
            if guess == target: 
                return "yay"
            elif guess > target:
                return "lower"
            elif guess < target: 
                return "higher"
            """include code for comparing user input with target number"""
        else: 
            # print("please input an integer between 1 and 100")
            # return validate_input()
            return "try again2"
    else: 
        # print("please input an integer")
        # return validate_input()
        return "try again1"

def print_message():
    """
    There are two reasons to print a message to the user
    1. validating input 
    2. higher, lower, correct

    """
    target = generate_number()
    while True:
        user_input = validate_input(target) 
        if user_input == "try again2":
            print("please input an integer")
        elif user_input == "try again1":
            print("please input an integer between 1 and 100")
        elif user_input == "higher":
            print("HIGHER!")
        elif user_input == "lower":
            print("LOWER!")
        else: 
            print("correct!\nThankyou for playing! Have a nice day :)")
            return False


    

#Try to have functions that only do one “thing” (e.g. print a message, validate user input, check what message to display)


    """running code & testcases"""
print_message()
