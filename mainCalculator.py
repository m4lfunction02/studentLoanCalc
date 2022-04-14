import income, interestRate, repaymentMethods, tools
from loanCalcs import increaseLoan
# Year 0 = first year of work, year -1 = last year of university, year starts April 6th


def run(repaymentMethod, repaymethodarg=0, printMonthly=False):
    loanTotal = 0
    totalBorrowed = 0
    totalRepaid = 0
    for year in range(-4, 30):
        annualIncome = income.linearCap(year)
        monthlyIncome = annualIncome / 12
        annualInterest = interestRate.constantCurrent(annualIncome, year)
        monthlyInterest = (1 + annualInterest) ** (1 / 12) - 1

        for month in range(12):
            repayment = repaymentMethod(monthlyIncome, repaymethodarg)
            if repayment >= loanTotal:
                repayment = loanTotal
            loanTotal -= repayment
            totalRepaid += repayment

            loanTotal *= monthlyInterest + 1

            borrow = increaseLoan(year, month)
            loanTotal += borrow
            totalBorrowed += borrow

            if printMonthly:
                print(f"Year: {year:>2}, Month: {month:>2}, Loan: {loanTotal:>9.2f}, Income: {monthlyIncome:>8.2f}, Repayment: {repayment:>7.2f}, Borrowed: {borrow:>8.2f}")
            if loanTotal == 0 and year >= 0:
                return(totalRepaid, totalBorrowed)
    return(totalRepaid, totalBorrowed)

mandatoryRepay, totalBorrowed = run(repaymentMethods.mandatory)

minFixedRepay = tools.bisect(run, repaymentMethods.constant, mandatoryRepay-0.01)
minTotalPercent = tools.bisect(run, repaymentMethods.totalPercentage, mandatoryRepay-0.01, 100)
minPartial = tools.bisect(run, repaymentMethods.partialPercentage, mandatoryRepay-0.01, 100)

print(f"You plan to borrow £{int(totalBorrowed):,d}")
print(f"If you make the minimum repayments you will repay £{int(mandatoryRepay):,d}")
if minFixedRepay is None:
    print(f"There is no way you can pay less than this with your current income.")
else:
    if minTotalPercent is None:
        print(f"To save money, each month, repay whichever is higher of your mandatory minimum repayment or £{int(minFixedRepay):,d}")
    else:
        print("To repay less money do one of the following:")
        print(f"1) Each month, repay whichever is higher of your mandatory minimum repayment or £{int(minFixedRepay):,d}")
        print(f"2) Each month, repay whichever is higher of your mandatory minimum repayment or {minTotalPercent:.2f}% of your income that month")
    if minPartial is not None:
        print(f"3) Each month, repay whichever is higher of your mandatory minimum repayment or {minPartial:.2f}% of your income over £2,274 that month")

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
        repaid, borrowed = run(repaymentMethods.constant,repayAmount,True)
        print(f"Total repayment: £{int(repaid):,d}, Total borrowed: £{int(borrowed):,d}, Total interest: £{int(repaid-borrowed):,d}")
        readInput()
    elif inputNo == 2:
        defaultRepay = minTotalPercent
        try:
            repayPercent = float(input(f"Type the percentage of your total income (omitting '%') you want to repay each month, default is {defaultRepay:.2f}: "))
        except ValueError:
            repayPercent = defaultRepay
        repaid, borrowed = run(repaymentMethods.totalPercentage,repayPercent,True)
        print(f"Total repayment: £{int(repaid):,d}, Total borrowed: £{int(borrowed):,d}, Total interest: £{int(repaid-borrowed):,d}")
        readInput()
    elif inputNo == 3:
        defaultRepay = minPartial
        try:
            repayPercent = float(input(f"Type the percentage of your income over £2274 (omitting '%') you want to repay each month, default is {defaultRepay:.2f}: "))
        except ValueError:
            repayPercent = defaultRepay
        repaid, borrowed = run(repaymentMethods.partialPercentage,repayPercent,True)
        print(f"Total repayment: £{int(repaid):,d}, Total borrowed: £{int(borrowed):,d}, Total interest: £{int(repaid-borrowed):,d}")
        readInput()
    else:
        print("Invalid input")
        readInput()

readInput()