def constantCurrent(annualIncome, year, RPI=0.015):
    if year < 0 or annualIncome >= 27_296:
        return(RPI+0.03)
    else:
        return(RPI)