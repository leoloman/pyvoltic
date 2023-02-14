import math

def poisson_calc_g(x:float, lam:float):
    """
    Probability generating function for poisson distribution
    
    args:
        x: float - value to obtain the result from
        lam: float - 
    """
    
    return math.e**(lam * (x-1)) 

def poisson_calc_g1(x:float, lam:float):
    """
    First derivative Probability generating function for poisson distribution
    
    args:
        x: float - value to obtain the result from
        lam: float - 
    """
    
    return lam * math.e**(lam * (x-1)) 

def poisson_calc_g2(x:float, lam:float):
    """
    Second derivative Probability generating function for poisson distribution
    
    args:
        x: float - value to obtain the result from
        lam: float - 
    """
    return (lam**2) * math.e**(lam * (x-1)) 