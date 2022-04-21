def constant(annualIncome, year, RPI=1.5):
    RPIfraction = RPI/100
    if year < 0 or annualIncome >= 27_296:
        return(RPIfraction+0.03)
    else:
        return(RPIfraction)


