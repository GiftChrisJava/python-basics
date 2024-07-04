class Loan:
    def __init__(self, annualInterestRate = 2.5,
    numberOfYears = 1, loanAmount = 100, borrower= ""):
        self.__annualInterestRate = annualInterestRate
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanAmount
        self.__borrower = borrower
        
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate
        
    def getBorrower(self):
        return self.__borrower
    def setBorrower(self, borrower):
        self.__borrower = borrower
        
    def getNumberOfYears(self):
        return self.__numberOfYears
    def setNumberOfYears(self, numberOfYears):
        self.__numberOfYears = numberOfYears
        
    def getLoanAmount(self):
        return self.__loanAmount
    def setLoanAmount(self, loanAmount):
        self.__loanAmount = loanAmount
        
    def getMonthlyPayment(self):
        # devide annual interest by 100 and multiply by 12
        monthlyInterestRate = self.__annualInterestRate / 1200
        
        monthlyPayment = self.__loanAmount * monthlyInterestRate / (1 -(1 / (1 + monthlyInterestRate) ** (self.__numberOfYears * 12)))
        return monthlyPayment
    
    def getTotalPayment(self):
        totalPayment = self.getMonthlyPayment() * \
            self.__numberOfYears * 12
            
        return totalPayment       