from Loan import Loan

def main():
    # enter yearly interest rate
    annualInterestRate = eval(input("Enter yearly interest rate, eg 7.25 : "))
    
    # enter number of years
    numberOfYears =  eval(input("Enter number of years : "))
    
    # enter loan amount 
    loanAmount = eval(input("Enter loan amount : "))
    
    borrower = input("Enter borrower's name : ")
    
    
    loan = Loan(annualInterestRate, numberOfYears, loanAmount, borrower)
    
    print("The loan is for", loan.getBorrower())
    print("The monthly payment is", format(loan.getMonthlyPayment(), ".2f"))
    print("The total payment is", format(loan.getTotalPayment(), ".2f"))
    
main()