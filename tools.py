def bisect(f, ff, target, max=1e9):
    eps = 0.001
    a = 1e-9
    b = max
    if (f(ff, a)[0] - target) * (f(ff, b)[0] - target) > 0:
        return(None)
    while b - a > eps:
        c = (a + b) / 2
        if f(ff, c)[0] - target == 0:
            return c
        elif (f(ff, c)[0] - target) * (f(ff, a)[0] - target) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2