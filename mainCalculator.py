import income, interestRate, repaymentMethods, tools
from loanCalcs import borrow
# Year 0 = first year of work, year -1 = last year of university, year starts April 6th

#Assumptions
startingSalary = float(input("Starting salary (omit '£'): ")) 
salaryGrowthRate = float(input("Salary annual growth rate (omit '%'): ")) #%
RPI = float(input("Retail price index (omit '%'): "))

#Settings
def annualIncome(year):
    return(income.percGrowth(year, startingSalary, salaryGrowthRate))

def annualInterest(year):
    return(interestRate.constant(annualIncome(year), year, RPI))

#Simulate entire loan
def simulate(repaymentMethod, printInfo=False):
    currentLoanAmount = 0
    totalBorrowed = 0
    totalRepaid = 0
    #Loop through each year
    for year in range(-4, 30):
        monthlyIncome = annualIncome(year) / 12
        monthlyInterest = (1 + annualInterest(year)) ** (1 / 12) - 1

        #Loop through each month
        for month in range(12):
            #Add interest
            currentLoanAmount *= monthlyInterest + 1

            #Calculate repayment amount
            if year >= 1:
                repayment = min(repaymentMethod(monthlyIncome), currentLoanAmount)
            else:
                repayment = 0
            #Repay 
            currentLoanAmount -= repayment
            totalRepaid += repayment

            #Calulate amount to borrow
            borrowAmount = borrow(year, month)
            #Borrow
            currentLoanAmount += borrowAmount
            totalBorrowed += borrowAmount

            if printInfo:
                print(f"Year: {year:>2} Month: {month:>2} Loan: {currentLoanAmount:>9.2f} Income: {monthlyIncome:>8.2f} Repayment: {repayment:>7.2f} Borrowed: {borrowAmount:>8.2f}")
            
            #If loan paid off, end loop
            if currentLoanAmount == 0 and year >= 0:
                if printInfo:
                    print(f"Total repayment: £{int(totalRepaid):,d} Total borrowed: £{int(totalBorrowed):,d} Extra repaid: £{int(totalRepaid-totalBorrowed):,d}")
                return(totalRepaid, totalBorrowed)

    #End loop after 30 years is up (loan not fully repaid)
    if printInfo:
        print(f"Total repayment: £{int(totalRepaid):,d} Total borrowed: £{int(totalBorrowed):,d} Extra repaid: £{int(totalRepaid-totalBorrowed):,d}")
    return(totalRepaid, totalBorrowed)

#Calculations for mandatory repayments
mandatoryRepay, totalBorrowed = simulate(repaymentMethods.mandatory)
print(f"You plan to borrow £{int(totalBorrowed):,d}")
print(f"If you make the minimum repayments you will repay £{int(mandatoryRepay):,d}")

#Functions that return the total repaid amount for a given repayment method, where the repayment amount/% can be varied
def constantRepayAmount(fixedMonthlyRepayment, printInfo=False):
    def repayMethod(monthlyIncome):
         return(repaymentMethods.constant(monthlyIncome, fixedMonthlyRepayment))
    return(simulate(repayMethod, printInfo)[0]) #Only return total repaid

def totalPercentRepayAmount(repayPercent, printInfo=False):
    def repayMethod(monthlyIncome):
         return(repaymentMethods.totalPercentage(monthlyIncome, repayPercent))
    return(simulate(repayMethod, printInfo)[0]) #Only return total repaid

def partialPercentRepayAmount(repayPercent, printInfo=False):
    def repayMethod(monthlyIncome):
         return(repaymentMethods.partialPercentage(monthlyIncome, repayPercent))
    return(simulate(repayMethod, printInfo)[0]) #Only return total repaid

#Calculate the minimum repayment amounts or % for each method
minFixedRepay = tools.bisect(constantRepayAmount, mandatoryRepay-0.01)
minTotalPercent = tools.bisect(totalPercentRepayAmount, mandatoryRepay-0.01, 100)
minPartial = tools.bisect(partialPercentRepayAmount, mandatoryRepay-0.01, 100)

#Display results
if minFixedRepay is None:
    simulate(repaymentMethods.mandatory, printInfo=True)
    print(f"You should make only the mandatory repayments (see above)")
else:
    if minTotalPercent is None:
        print(f"1) To save money, each month, repay at least whichever is higher of your mandatory minimum repayment or £{int(minFixedRepay):,d}")
    else:
        print("To repay less money do one of the following:")
        print(f"1) Each month, repay at least whichever is higher of your mandatory minimum repayment or £{int(minFixedRepay):,d}")
        print(f"2) Each month, repay at least whichever is higher of your mandatory minimum repayment or {minTotalPercent:.2f}% of your income that month")
    if minPartial is not None:
        print(f"3) Each month, repay at least whichever is higher of your mandatory minimum repayment or {minPartial:.2f}% of your income over £2,274 that month")

#Display more info, as requested by user
if minFixedRepay is not None:
    def readInput():
        inputNo = int(input("Type a number to explore that repayment method, or 0 to exit: "))
        if inputNo == 0:
            return(None)
        elif inputNo == 1:
            defaultRepay = minFixedRepay
            try:
                repayAmount = float(input(f"Type the amount of money (omitting '£') you want to repay each month, default is {defaultRepay:.2f}: "))
            except ValueError:
                repayAmount = defaultRepay
            totalRepaid = constantRepayAmount(repayAmount, printInfo=True)
            print(f"Amount saved vs mandatory repayments £{int(mandatoryRepay - totalRepaid):,d}")
            readInput()
        elif inputNo == 2:
            defaultRepay = minTotalPercent
            try:
                repayPercent = float(input(f"Type the percentage of your total income (omitting '%') you want to repay each month, default is {defaultRepay:.2f}: "))
            except ValueError:
                repayPercent = defaultRepay
            totalRepaid = totalPercentRepayAmount(repayPercent, printInfo=True)
            print(f"Amount saved vs mandatory repayments £{int(mandatoryRepay - totalRepaid):,d}")
            readInput()
        elif inputNo == 3:
            defaultRepay = minPartial
            try:
                repayPercent = float(input(f"Type the percentage of your income over £2274 (omitting '%') you want to repay each month, default is {defaultRepay:.2f}: "))
            except ValueError:
                repayPercent = defaultRepay
            totalRepaid = partialPercentRepayAmount(repayPercent, printInfo=True)
            print(f"Amount saved vs mandatory repayments £{int(mandatoryRepay - totalRepaid):,d}")
            readInput()
        else:
            print("Invalid input")
            readInput()

    readInput()
