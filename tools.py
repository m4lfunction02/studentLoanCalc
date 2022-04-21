def bisect(function, target, max=1e9):
    eps = 0.001

    #Solution lies between a and b
    a = 1e-9
    b = max

    #If no solution return None
    if (function(a) - target) * (function(b) - target) > 0:
        return(None)

    #Main bisect loop, narrows down interval until interval is smaller than eps, then returns midpoint as function root
    while b - a > eps:
        c = (a + b) / 2
        if function(c) - target == 0:
            return(c)
        elif (function(c) - target) * (function(a) - target) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2