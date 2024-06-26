import random
import time

correctCount = 0 #count correct answers
count = 0 # count the number of questions
NUMBER_OF_QUESTIONS = 5

startTime = time.time() # Get start time

while count < NUMBER_OF_QUESTIONS :
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)

    if number1 < number2 : 
        number1, number2 = number2, number1

    answer = eval(input("What is " + str(number1) + " - " + str(number2) + " ? >> "))
    
    if number1 - number2 == answer :
        print("You are correct!")
        correctCount += 1
    else :
        print("Your answer is wrong.\n", number1, "-", number2, "is", number1 - number2)
        
    count += 1 #increment

endTime = time.time() # get end time
testTime = int(endTime - startTime)

print("Correct count is", correctCount, "out of", NUMBER_OF_QUESTIONS, "which represents",
      round((correctCount / NUMBER_OF_QUESTIONS) * 100, 0), "%\nTest time is", testTime, "seconds"
      )
