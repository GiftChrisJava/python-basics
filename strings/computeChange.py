#receive the amount
amount = eval(input("Enter an amount, eg 11.56 : "))

#convert the amount to cents
remainingAmount = int(amount * 100)

# the number of 1 dollars
mumberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100


# find the amount of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount %= 25

# find the number of dimes
numberOfDimes = remainingAmount // 10
remainingAmount %=10

#find the number of nickles
numberOfNickles = remainingAmount // 5
remainingAmount %= 5

numberOfPennies = remainingAmount

#displat the result
print("your amount ", amount, " consits of \n",
      "\t", mumberOfOneDollars, " dollars\n",
      "\t", numberOfQuarters, " quarters\n",
      "\t", numberOfDimes, " dimes\n",
      "\t", numberOfNickles, " nickles\n",
      "\t", numberOfPennies, " pennies"
      ) 