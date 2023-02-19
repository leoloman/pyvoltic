"""
This script is for models which are not written by Volz / Miller but could be useful and are a part of the EBCM family.
"""
import scipy.integrate as sp_int
import numpy as np

from pyvoltic.classes import VolzFramework
from pyvoltic.results import SEIRSRResults


class SEIRSR(VolzFramework):
    """
    Instantiate an SEIR compartmental on a static random network
    Alota et al (2020)
    Ref: https://link.springer.com/article/10.1007/s11538-020-00769-0
    """
    
    __doc__ += VolzFramework.__doc__
    
    def _set_initial_states(self, epsilon):
        """
        Set the inital state for the ode solver
        
        args:
            epsilon: float or tuple, when a float the starting state for both E and I is equal. Whereas if you pass a tuple the first entry will be proportion of E and the second entry the proportion of I
        """
        if isinstance(epsilon, tuple):
            epsilon_e = epsilon[0]
            epsilon_i = epsilon[1]
            epsilon = (epsilon[0] + epsilon[1])
            
            return [1 - epsilon, # theta
              (epsilon_i)/(1- epsilon) ,# piI
              (epsilon_e)/(1- epsilon)  , # pi E
             (1- (2*epsilon))/(1- epsilon)   , # pi S
            epsilon_e, # E
               epsilon_i , # I
               ] 
        else:
        
            return [1 - epsilon, # theta
              (epsilon/2)/(1- epsilon) ,# piI
              (epsilon/2)/(1- epsilon)  , # pi E
             (1- 2*epsilon)/(1- epsilon)   , # pi S
            epsilon/2, # E
               epsilon/2 , # I
               ] 
    
    def calc_r0(self, r, mu):
        """
        Calculate r0 - the average number of infections per person
        
        Ref: 3.2 - https://link.springer.com/article/10.1007/s11538-020-00769-0
        
        args:
            r:float - probability of transmission
            mu: float - recovery rate
            
        returns:
            r0: float
        """
        return (r/ (r + mu)) * (self.calc_g2(1)/self.calc_g1(1))
    

    def ode(self, x, t, rr, aa, mm, calc_g, calc_g1, calc_g2):
        y = list(range(6))
        # dot theta
        y[0] = -rr *  x[1] * x[0]
        # pi I
        y[1] = aa *  x[2] - rr * x[1] * (1 - x[1]) - mm * x[1]
        # pi E
        y[2] = rr * x[1] * x[3] * x[0] * (calc_g2(x[0])/calc_g1(x[0])) - aa * x[2] +rr * x[2] * x[1]
        # pi s
        y[3] = rr * x[1] * x[3] * (1 - x[0] * (calc_g2(x[0])/calc_g1(x[0])))
        
        # S = calc_g(x[0])
        
        # E
        y[4] = rr * x[1] * x[0] * calc_g1(x[0]) - aa * x[4]
        # I
        y[5] = aa * x[4] - mm * x[5]
                                   
        return y
        
    def run_simulation(self, r:float, a:float, mu:float, epsilon:float, timesteps:int):
        """
        r: probabiltiy of transmission
        a: rate of moving from E to I
        mu: recovery rate
        epsilon: float or tuple, when a float the starting state for both E and I is equal. Whereas if you pass a tuple the first entry will be proportion of E and the second entry the proportion of I
        timesteps: int - number of timesteps
        
        
        """
        
        time = list(range(timesteps))
        
        r0 = self.calc_r0(r, mu)
        
        initial_state = self._set_initial_states(epsilon)
        
        output = sp_int.odeint(
            self.ode,
            initial_state,
            time,
            args=(r, a, mu,  self.calc_g, self.calc_g1, self.calc_g2),
        )
        # create S compartment
        S = np.array([[self.calc_g(x)] for x in output[:,0]])
        output = np.hstack((output, S))
        # create R compartment
        # 1 - S - I - E
        R = np.array([[1 - x[6] - x[5] - x[4]] for x in output])
        output = np.hstack((output, R))    
        
        return SEIRSRResults(output, dict(r=r, a=a, mu=mu, epsilon=epsilon), r0)