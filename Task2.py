"""
input: user guess
output: higher or lower or correct

requirements: 
- check for valid inputs 
"""

#things to do
#validate user input
#generate target number
#allow user to guess 
#compare guess with target number
def valid_input():
    x = int(input())
    if x > 1 and x < 100:
        print("yay") #assuming that 1 and 100 are not included since "between"
        return x
    else: 
        print("please input an integer between 1 and 100")
        valid_input()
    

valid_input()
