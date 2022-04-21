#Define monthly repayment functions

#Mandatory minimum repayments
def mandatory(monthlyIncome):
    incomeAboveThreshold = max(0, monthlyIncome - 2_274)
    repaymentFraction = 0.09 
    amount = incomeAboveThreshold * repaymentFraction
    return(amount)

#Pay a constant amount per month, regardless of income (if income is less than the fixed repayment, then the entire income is paid)
def constant(monthlyIncome, fixedMonthlyRepayment):
    chosenAmount = min(fixedMonthlyRepayment, monthlyIncome) #Can't repay more than income
    minimumAmount = mandatory(monthlyIncome)
    return(max(minimumAmount, chosenAmount)) #Must repay minimum at least
 
#Repay a percentage of the monthly income
def totalPercentage(monthlyIncome, repaymentPercentage):
    repaymentFraction = repaymentPercentage/100 #Convert percentage to fraction
    chosenAmount = monthlyIncome * repaymentFraction
    minimumAmount = mandatory(monthlyIncome)
    return(max(minimumAmount, chosenAmount)) #Must repay minimum at least

#Repay a percentage of the monthly income over 2274 (similar to mandatory, but with a different repayment percentage)
def partialPercentage(monthlyIncome, repaymentPercentage):
    incomeAboveThreshold = max(0, monthlyIncome - 2_274)
    repaymentFraction = repaymentPercentage/100 #Convert percentage to fraction
    chosenAmount = incomeAboveThreshold * repaymentFraction
    minimumAmount = mandatory(monthlyIncome)
    return(max(minimumAmount, chosenAmount)) #Must repay minimum at least