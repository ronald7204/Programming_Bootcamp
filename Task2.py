"""
input: user guess
output: higher or lower or correct

requirements: 
- check for valid inputs 
"""

#things to do

#generate target number
#allow user to guess 
#compare guess with target number

print('hello1')
input()
def valid_input():
    x = input()
    if x > 1 and x < 100: #assuming that 1 and 100 are not included since "between"
        pass
    else: 
        raise KeyError
    print("hello2")

valid_input()
print('hello3')