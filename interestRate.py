def constant(annualIncome, year, RPI=1.5):
    RPIfraction = RPI/100
    #During study, or if income is above 49_130, then interest is RPI + 3%
    if year < 0 or annualIncome > 49_130:
        return(RPIfraction+0.03)
    #If income is below 27_295, then interest is RPI + 0%
    elif annualIncome <= 27_295:
        return(RPIfraction)
    #If income is between 27_295 and 49_130, then interest is RPI + x, where x increases linearly from 0% at 27_295 to 3% at 49_130
    else:
        additionalInterest = (annualIncome - 27_295)/(49_130 - 27_295)*0.03
        return(RPIfraction + additionalInterest)


