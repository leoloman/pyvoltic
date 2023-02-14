import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class SimResults(ABC):
    
    def __init__(self, output, param_dic, r0 = None):
        self.output = output
        self.param_dic = param_dic
        self.r0 = r0

    @abstractmethod
    def SIR_graph(self):
        pass
    
    @abstractmethod
    def cumulative_incidence(self):
        pass
    
    @abstractmethod
    def full_simulation(self):
        pass
    
    
   