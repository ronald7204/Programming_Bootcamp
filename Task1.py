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


intuition -> example: [8,1,3,4] list can be concatenated by adding 8000+100+30+4 -> which would result in 8134
this can be achieved by multiplying each element by 10 to a power relative to its position, and adding it all up using a variable.
"""





def concatenator(input):
    temp = 0 #creating a variable to concatenate a list into 
    power = len(input) - 1 #the minus 1 ensures that when the element is multiplied by 10 and the power isn't too high, for example #[8,1,3,4] would result in 81340 without the minus 1
    if len(input) > 0: # to make sure that the input is not empty
        for i in input: #acesses each element in the list from left to right
            temp += i*(10**power) #multiplies accessed element with 10 to a power (which is relative to the elements position in the list) and assigns the value to a variable
            power -= 1 #reduces the power by 1 to account for moving onto the next element in the list
        return temp
    

ex1 = []
ex2 = [1,2,3,4,5,67,77,9]
ex3 = [6,5,4]
ex4 = [1,3,4]
print(concatenator(ex1)) #--> return none because there are no elements to concatenate in the input list
print(concatenator(ex2))
print(concatenator(ex3))
print(concatenator(ex4))