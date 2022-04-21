#Income is pre-tax
def linearCap(year, base=25_000, *args):
    if year < 0:
        income = 0
    else:
        income = base + 3_500 * year

    if income > 95_000:
        income = 95_000
    return(income)

def percGrowth(year, base=25_000, growthperc=3):
    if year < 0:
        income = 0
    else:
        income = base*(1+growthperc/100)**year
    return(income)
