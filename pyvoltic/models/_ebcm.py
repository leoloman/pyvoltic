import scipy.integrate as sp_int
import numpy as np
from ..results import EBCMResults, DFDResults, NEResults, SRResults
from ..classes import VolzFramework

import math


class EBCM(VolzFramework):
    """
    Instantiate the first Edge Based Compartmental Model

    Ref https://royalsocietypublishing.org/doi/10.1098/rsif.2011.0403
        https://arxiv.org/pdf/1106.6320
        https://arxiv.org/pdf/0909.4485.pdf
    """

    __doc__ += VolzFramework.__doc__

    def _set_initial_states(self, epsilon):
        """
        Set the initial states
        """
        return [1 - epsilon, 0]

    def run_simulation(self, beta: float, gamma: float, epsilon: float, timesteps: int):
        """
        Run a single simulation using scipy odeint function
        """

        r0 = self.calc_r0(beta, gamma)

        initial_state = self._set_initial_states(epsilon)

        time = list(range(timesteps))

        output = sp_int.odeint(
            self.ode,
            initial_state,
            time,
            args=(beta, gamma, self.calc_g, self.calc_g1, self.calc_g2),
        )
        # add susceptible
        output = np.hstack((output, np.array([[self.calc_g(x)] for x in output[:, 0]])))
        # add infected
        output = np.hstack((output, np.array([[1 - x[1] - x[2]] for x in output])))

        return EBCMResults(output, dict(beta=beta, gamma=gamma, epsilon=epsilon), r0)

    def calc_r0(self, beta: float, gamma: float):
        return (beta / (beta + gamma)) * (
            (self.calc_g1(1) ** 2 - self.calc_g1(1)) / self.calc_g1(1)
        )

    def ode(self, x, t, beta, gamma, calc_g, calc_g1, calc_g2):
        """
        Ref https://royalsocietypublishing.org/doi/10.1098/rsif.2011.0403
            https://arxiv.org/pdf/1106.6320
            https://arxiv.org/pdf/0909.4485.pdf
        """

        y = list(range(2))

        y[0] = -beta * x[0] + beta * (calc_g1(x[0]) / calc_g1(1)) + gamma * (1 - x[0])
        S = calc_g(x[0])
        I = 1 - S - x[1]
        y[1] = gamma * I

        return y


class MFSHEBCM(VolzFramework):

    """
    Instantiate the Mean Field Social Hetergoenity Edge Based Compartmental Model

    Ref https://arxiv.org/pdf/1106.6320 page 7

    """

    __doc__ += VolzFramework.__doc__

    def _set_initial_states(self, epsilon: float):
        """
        Set the initial states
        """
        return [1 - epsilon, 0]

    def run_simulation(self, beta: float, gamma: float, epsilon: float, timesteps: int):
        """
        Run a single simulation using scipy odeint function
        """

        r0 = self.calc_r0(beta, gamma)

        initial_state = self._set_initial_states(epsilon)

        time = list(range(timesteps))

        output = sp_int.odeint(
            self.ode,
            initial_state,
            time,
            args=(beta, gamma, self.calc_g, self.calc_g1, self.calc_g2),
        )
        # add susceptible
        output = np.hstack((output, np.array([[self.calc_g(x)] for x in output[:, 0]])))
        # add infected
        output = np.hstack((output, np.array([[1 - x[1] - x[2]] for x in output])))

        return EBCMResults(output, dict(beta=beta, gamma=gamma, epsilon=epsilon), r0)

    def calc_r0(self, beta: float, gamma: float):
        return (beta / gamma) * (self.calc_g1(1) ** 2 / self.calc_g1(1))

    def ode(self, x, t, beta, gamma, calc_g, calc_g1, calc_g2):
        """
        Ref https://arxiv.org/pdf/1106.6320 page 7
        """

        y = list(range(2))

        y[0] = (
            -beta * x[0]
            + beta * ((x[0] ** 2 * calc_g1(x[0])) / calc_g1(1))
            - x[0] * gamma * math.log(x[0])
        )
        S = calc_g(x[0])
        I = 1 - S - x[1]
        y[1] = gamma * I

        return y


class DynamicFixedDegree(VolzFramework):

    """
    The Dynamic Fixed Degree is equivalent to the SIRNE model, it interpolates between a regular Configuration Model and the Mean Field Social Hetergoenity Model. Nodes are assigned degree $k$ as before and pairs stubs randomly. As time progresses, edges break, the freed stub immediatley join with stubs from other edges that break. A process called edge swapping. The rate an edge breaks is $\eta$
    
    https://arxiv.org/pdf/1106.6320.pdf page 8
    
    """
    __doc__ += VolzFramework.__doc__
    def _set_initial_states(self, epsilon: float, eta: float):
        """
        Set the initial states
        """
        # not 100% sure if correct
        theta = 1 - epsilon
        pi_S = (theta * self.calc_g1(theta)) / self.calc_g1(1)
        pi_R = 0
        pi_I = 1 - pi_S - pi_R
        psi_S = theta* pi_S
        psi_I =  theta* pi_I
        return [theta, psi_I, psi_S, 0, 0]  # psi i  # psi s  # pi r  # r

    def run_simulation(self, beta: float, eta: float, gamma: float, epsilon: float, timesteps: int):
        """
        Run a single simulation using scipy odeint function
        """

        initial_states = self._set_initial_states(epsilon, eta)

        r0 = self.calc_r0(beta, eta, gamma)

        time = list(range(timesteps))

        output = sp_int.odeint(
            self.ode,
            initial_states,
            time,
            args=(beta, eta, gamma, self.calc_g, self.calc_g1, self.calc_g2),
        )
        
        susceptible = np.array([[self.calc_g(x)] for x in output[:,0]])
        
        output = np.hstack((output, susceptible)) # susceptible col
       
        infected = np.array([[1 - x[4] - x[5]] for x in output])
        output = np.hstack((output, infected ))
        
        pi_S = np.array([[x*self.calc_g1(x)/self.calc_g1(1)] for x in output[:,0]])
        output = np.hstack((output, pi_S ))
        pi_I = np.array([[1 - x[3] - x[7]] for x in output])
        output = np.hstack((output, pi_I ))
        # implement DFDResults
        # add all aspects of the compartments
        return DFDResults(output, dict(beta = beta, eta = eta, gamma = gamma), None)
        # return DFDResults(output, dict(beta = beta, eta = eta, gamma = gamma, epsilon = epsilon), r0
        # add susceptible
        # output = np.hstack((output, np.array([[self.calc_g(x)] for x in output[:,0]])))
        # add infected
        # output = np.hstack((output, np.array([[1 - x[1] - x[2] ] for x in output])))

        # return EBCMResults(output, dict(beta = beta, gamma = gamma), r0)

    def ode(self, x, t, beta, eta, gamma, calc_g, calc_g1, calc_g2):
        """
        Ref https://arxiv.org/pdf/1106.6320 page 7
        """
        # x[0] theta
        # x[1] psi i
        # x[2] psi s
        # x[3] pi r
        # x[4] r
        y = list(range(5))
        # theta
        y[0] = -beta * x[1]

        pi_S = (x[0] * calc_g1(x[0])) / (calc_g1(1))

        pi_I = 1 - x[3] - pi_S
        # pi R
        y[3] = gamma * pi_I

        y[2] = (
            -beta * x[1] * x[2] * (calc_g2(x[0]) / calc_g1(x[0]))
            + eta * x[0] * pi_S
            - eta * x[2]
        )

        y[1] = (
            beta * x[1] * x[2] * (calc_g2(x[0]) / calc_g1(x[0]))
            + eta * x[0] * pi_I
            - (beta + gamma + eta) * x[1]
        )

        S = calc_g(x[0])

        I = 1 - S - x[4]

        y[4] = gamma * I

        return y

    def calc_r0(self, beta, eta, gamma):
        return (beta / (beta + eta + gamma)) * (
            ((eta + gamma) / gamma)
            * ((self.calc_g1(1) ** 2 * self.calc_g1(1)) / self.calc_g1(1))
            + (eta / gamma)
        )
