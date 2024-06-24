#enter an integer
userInput = input("Enter am integer eg 1156 : ")

word = str(userInput)

dollars = word[:2]
cents = word[2:]

print(f"{userInput} represents {dollars} dollars and {cents} cents")