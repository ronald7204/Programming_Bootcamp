""" 
Programming Task #1
input: [8,1,3,4]
output: 8134 (as int)

requirements for code: 
- input must be a list, output must be an integer
- no conversion/casting
- A comment at the top of the file introducing how the code works (to a beginner) and why it works (i.e. the intuition).
- Comment and documentation that explain the purpose of sections/lines of code where appropriate.
- some examples or test cases demonstrating that it works.
- avoid global variables 
- code should be simple and intuitive
"""


def concatenator(input):
    temp = 0 #creating a variable to concatenate a list into 
    power = len(input) - 1
    if len(input) > 0:
        for i in input: 
            temp += i*(10**power)
            power -= 1
        print(temp)
    else: 
        print("input list is empty")

ex1 = []
ex2 = [1,2,3,4,5,67,77,9]
ex3 = [6,5,4]
ex4 = [1,3,4]
concatenator(ex1)
concatenator(ex2)
concatenator(ex3)
concatenator(ex4)