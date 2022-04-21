#Income is pre-tax

#Increase income by fixed amount per year
def linear(year, base=25_000, annualIncrease=3_500):
    if year < 0:
        income = 0
    else:
        income = base + annualIncrease * year
    return(income)

#Increase income by percentage per year
def percGrowth(year, base=25_000, growthperc=3):
    growthFraction = 1 + growthperc/100
    if year < 0:
        income = 0
    else:
        income = base*(growthFraction**year)
    return(income)
