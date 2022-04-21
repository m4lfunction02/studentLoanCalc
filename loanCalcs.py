def borrow(year, month):
    addLoan = 0
    if year == -4:
        if month == 6: # October
            addLoan += 2034.78 # Maintenance
            addLoan += 2312.50 # Tuition 
        elif month == 9: # January
            addLoan += 2034.78 # Maintenance
        elif month == 10: # February
            addLoan += 2312.50 # Tuition
    elif year < 0:
        if month == 1: # May
            addLoan += 2096.44 # Maintenance
            addLoan += 4625 # Tuition
        if month == 6: # October
            addLoan += 2034.78 # Maintenance
            addLoan += 2312.50 # Tuition 
        elif month == 9: # January
            addLoan += 2034.78 # Maintenance
        elif month == 10: # February
            addLoan += 2312.50 # Tuition
    elif year == 0:
        if month == 1: # May
            addLoan += 2096.44 # Maintenance
            addLoan += 4625 # Tuition
    return(addLoan)