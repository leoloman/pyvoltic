def powerlaw_p_vec(alpha:float, max_deg:int):
    """
    Create the power law probability vector, required for the powerlaw probability generating function below
    """
    dist = [0]*(max_deg+1)
    alpha = float(alpha)
    denom = 0.0
    for i in range(1, max_deg+1):
        denom += i**(-1*alpha)
    for k in range(1, max_deg+1):
        dist[k] = k**(-1*alpha)/denom
    
    return dist

def powerlaw_calc_g(x:float, p_vec: dict):
    """
    Probability generating function for generic powerlaw distribution
    
    args:
        x: float - value to obtain the result from
        p_vec: dict - result from powerlaw_p_vec function
    """
    g_val = 0
    for k in range(len(p_vec)):
        g_val = g_val + p_vec[k]*x**(k)
    return g_val

def powerlaw_calc_g1(x:float, p_vec: dict):
    """
    First derivative Probability generating function for generic powerlaw distribution
    
    args:
        x: float - value to obtain the result from
        p_vec: dict - result from powerlaw_p_vec function
    """
    g_val = 0
    for k in range(len(p_vec)):
        g_val = g_val + (k)*p_vec[k]*x**(k-1)
    return g_val

def powerlaw_calc_g2(x:float, p_vec: dict):
    """
    Second derivate Probability generating function for generic powerlaw distribution
    
    args:
        x: float - value to obtain the result from
        p_vec: dict - result from powerlaw_p_vec function
    """
    g_val = 0
    for k in range(len(p_vec)):
        g_val = g_val + (k)*(k-1)*p_vec[k]*x**(k-2)
    return g_val