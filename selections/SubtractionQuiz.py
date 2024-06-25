import random
# generate 2 random single-digit integers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

if number1 < number2 : 
    number1, number2 = number2, number1 # swap the numbers
    
# prompt user to enter an answer
answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

# check answer and display
if number1 - number2 == answer :
    print("You are correct")
else : 
    print("You got it wrong.\n", number1, "-", number2, "is", number1 - number2)