#Define monthly repayment functions

def mandatory(monthlyIncome, *args):
    return(max(0, monthlyIncome - 2_274) * 0.09)

def constant(monthlyIncome, fixedMonthlyRepayment): # Pay a constant amount per month, regardless of income (if income is less than the fixed repayment, then the entire income is paid)
    return(max(mandatory(monthlyIncome), min(monthlyIncome, fixedMonthlyRepayment)))

def totalPercentage(monthlyIncome, repaymentPercentage): # Repay a percentage of the monthly income
    return(max(mandatory(monthlyIncome), monthlyIncome * (repaymentPercentage/100)))

def partialPercentage(monthlyIncome, repaymentPercentage): # Repay a percentage of the monthly income over 2274 (similar to mandatory, but with a different repayment percentage)
    return(max(mandatory(monthlyIncome), max(0, monthlyIncome - 2_274) * (repaymentPercentage/100)))