#Income is pre-tax
def linearCap(year):
    if year < 0:
        income = 0
    else:
        income = 25_000 + 3_500 * year

    if income > 95_000:
        income = 95_000
    return(income)