#enter name 
name = input("Enter employee's name : ")

# enter the number of hours worked
hoursWorked = eval(input("Enter the number of hours worked in a week : "))

# enter hourly pay rate
hourlyPayRate = eval(input("Enter hourly pay rate : "))

#federal tax
federalTaxWithholdingRate = eval(input("Enter federal tax withholding rate : "))

#state tax
stateTaxWithholdingRate = eval(input("Enter state tax withholding rate : "))

grossPay = hourlyPayRate * hoursWorked

fedralMoney = grossPay * federalTaxWithholdingRate
stateMoney = grossPay * stateTaxWithholdingRate

print("Employee Name : $", name, "\n",
      "Hours Worked : $", hoursWorked, "\n",
      "Pay Rate : $", hourlyPayRate, "\n",
      "Gross Pay : $", grossPay, "\n",
      "Deductions\n",
       "\tFederal Withholding (20%) : $", fedralMoney,  "\n",
       "\tState Withholding (9%) : $", stateMoney, "\n",
       "\tTotal Deduction : $", stateMoney + fedralMoney, "\n",
       "Net Pay : $", grossPay - (stateMoney + fedralMoney)
      )