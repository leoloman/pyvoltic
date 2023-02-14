import numpy as np
import matplotlib.pyplot as plt
from pyvoltic.classes import SimResults


class EBCMResults(SimResults):
    
    def SIR_graph(self):
        plt.plot(self.output[:,1], label = 'R')
        plt.plot(self.output[:,2], label = 's')
        plt.plot(self.output[:,3], label = 'I')
        plt.legend()
    
    def cumulative_incidence(self):
        plt.plot(self.output[:,1]+self.output[:,3], label = 'R')
        plt.legend()
    
    
    def full_simulation(self):
        plt.plot(self.output[:,0], label = 'theta')
        plt.plot(self.output[:,1], label = 'R')
        plt.plot(self.output[:,2], label = 'S')
        plt.plot(self.output[:,3], label = 'I')
        plt.legend()
        
        
class DFDResults(SimResults):
    
    def SIR_graph(self):
        pass
    
    def cumulative_incidence(self):
        pass
    
    def full_simulation(self):
        pass
    

class NEResults(SimResults):
    
    def SIR_graph(self, N:int = None, title:str = '', 
                 figsize:tuple = (12,5), log_scale:bool = False,
                caption = ''):
    
        fig, ax = plt.subplots(figsize =figsize)
        if (N == None):
            ax.plot(self.output[:,3], label = 'S')
            ax.plot(self.output[:,5],  label = 'I')
            ax.plot(1 - (self.output[:,5]+self.output[:,3]), alpha = 0.5, label= 'R')
            ax.set_ylabel('Proportion of Nodes')

        elif (isinstance(N, int)):
            ax.plot(self.output[:,3]*N, label = 'S')
            ax.plot(self.output[:,5]*N,  label = 'I')
            ax.plot(N - ((self.output[:,5]*N)+(self.output[:,3]*N)), alpha = 0.5, label= 'R')
            ax.set_ylabel('Number of Nodes')

        if log_scale:
            ax.set_yscale('log')

        plt.figtext(0.8, 0.01, caption, wrap=True, horizontalalignment='center', fontsize=12)
        plt.legend(title = 'Compartment')
        plt.show()
    
    
    def cumulative_incidence(self, title:str = '', color:str = 'black', linestyle:str = ':',label = 'Cumulative Incidence', figsize:tuple = (12,5)):
        """
        Cumulative Incidence plot of a single NE simulation

        args:
            title: str - title of plot
            color: str - color of line
            linestyle: str - linestyle
            label: str - label on legend
            figsize:tuple - plot size
        """
        
        fig, ax = plt.subplots(figsize =figsize)
        ax.plot(1 - (self.output[:,5]+self.output[:,3]) + self.output[:,5], 
                alpha = 0.5, 
                c = color,
                label= label, 
                ls = linestyle)
        ax.legend()
        ax.set_title(title)
        plt.show()
        
    def full_simulation(self, title: str = '', figsize:tuple = (12,5), log_scale:bool = False):
        fig, ax = plt.subplots(figsize =figsize)
        ax.plot(self.output[:,0], alpha =0.5, label = 'Fraction degree 1 nodes sus') # change of theta
        ax.plot(self.output[:,1], label = 'Prob Sus ego to infectious alter',
                )#change of p_infec 
        ax.plot(self.output[:,2], label = 'Prob Sus ego to Sus alter')# change of p_suscep 
        ax.plot(self.output[:,3], label = 'Frac S', ls = '--') #proportion of S
        ax.plot(self.output[:,4], label = 'Infectious ego with an alter of any state')# change of M_I 
        ax.plot(self.output[:,5], alpha = 0.5, label = 'Frac I', ls = '--') # change of I
        # recovered
        ax.plot(1 - (self.output[:,5]+self.output[:,3]), alpha = 0.5, label= 'Frac R', ls = '--')
        ax.plot(1 - (self.output[:,5]+self.output[:,3]) + self.output[:,5], alpha = 0.5, c = 'black',label= 'CS Incidennce', ls = ':')
        ax.legend(title = 'Compartments', bbox_to_anchor = (1.1,0.8))
        ax.set_title(title)
        ax.set_ylabel('Proportion')
        ax.set_xlabel('Time Step')
        if log_scale:
            ax.set_yscale('log')
        plt.show()
        
        
class SRResults(SimResults):
    
    def SIR_graph(self,  N:int = None, title:str = '', figsize:tuple = (12,5), log_scale:bool = False):
        fig, ax = plt.subplots(figsize =figsize)
        if (N == None):
            ax.plot(self.output[:,3], label = 'S')
            ax.plot(self.output[:,4],  label = 'I')
            ax.plot(1 - (self.output[:,4]+self.output[:,3]), alpha = 0.5, label= 'R')
            ax.set_ylabel('Proportion of Nodes')

        elif (isinstance(N, int)):
            ax.plot(self.output[:,3]*N, label = 'S')
            ax.plot(self.output[:,5]*N,  label = 'I')
            ax.plot(N - ((self.output[:,5]*N)+(self.output[:,3]*N)), alpha = 0.5, label= 'R')
            ax.set_ylabel('Number of Nodes')
        if log_scale:
            ax.set_yscale('log')
        plt.legend(title = 'Compartment')
        plt.show()
    
    
    def cumulative_incidence(self, title:str = '', color:str = 'black', linestyle:str = ':',label = 'Cumulative Incidence', figsize:tuple = (12,5)):
        """
        Cumulative Incidence plot of a single SR simulation

        args:
            output: np.array - result of a single SR simulation
            title: str - title of plot
            color: str - color of line
            linestyle: str - linestyle
            label: str - label on legend
            figsize:tuple - plot size
        """
        fig, ax = plt.subplots(figsize =figsize)
        ax.plot(1 - (self.output[:,4]+self.output[:,3]) + output[:,4], 
                alpha = 0.5, 
                c = color,
                label= label, 
                ls = linestyle)
        ax.legend()
        ax.set_title(title)
        plt.show()
        
    def full_simulation(self, title: str = '', figsize:tuple = (12,5), log_scale:bool = False):
        pass
    
    