import numpy as np
import matplotlib.pyplot as plt
from pyvoltic.classes import SimResults


class EBCMResults(SimResults):
    
    def SIR_graph(self, figsize  = (7,3)):
        fig = plt.figure(figsize = figsize, dpi = 200)
        ax = plt.subplot(ylim = [-0.05, 1.05])
        ax.plot(self.output[:,1], label = 'R', color = '#33A02C', linewidth = 2)
        ax.plot(self.output[:,2], label = 'S', color = '#003087', linewidth = 2)
        ax.plot(self.output[:,3], label = 'I', color = 'red', linewidth = 2)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_ylabel('Proportion\n')
        plt.tight_layout()
        plt.legend()
    
    def cumulative_incidence(self, title= 'Cumulative Incidence', figsize:tuple = (12,5)):
        fig = plt.figure(figsize = figsize, dpi = 200)
        ax = plt.subplot(ylim = [-0.05, 1.05])
        ax.plot(self.output[:,1]+self.output[:,3], linestyle = 'dashed', color= 'grey',
               linewidth = 2)
        ax.set_ylim(-0.05, 1.05)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_ylabel('Proportion\n')
        ax.set_title(title)
        plt.tight_layout()
        plt.rc('xtick', labelsize = 'small')
        # plt.legend()
        plt.show()
    
    def full_simulation(self,figsize  = (6,3)):
        fig = plt.figure(figsize = figsize, dpi = 200)
        ax = plt.subplot(ylim = [-0.05, 1.05])
        plt.plot(self.output[:,0], label = r'$\theta$', linestyle = 'dashed', color = 'grey', linewidth = 2)
        plt.plot(self.output[:,1], label = 'R', color = '#33A02C', linewidth = 2)
        plt.plot(self.output[:,2], label = 'S',color = '#003087', linewidth = 2)
        plt.plot(self.output[:,3], label = 'I', color = 'red', linewidth = 2)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_ylabel('Proportion\n')
        plt.tight_layout()
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
    
        fig = plt.figure(figsize = figsize, dpi = 200)
        ax = plt.subplot(ylim = [-0.05, 1.05])
        if (N == None):
            ax.plot(self.output[:,3], label = 'S',color = '#003087')
            ax.plot(self.output[:,5],  label = 'I',  color = 'red')
            ax.plot(1 - (self.output[:,5]+self.output[:,3]), alpha = 0.5, label= 'R', color = '#33A02C')
            ax.set_ylabel('Proportion of Nodes')

        elif (isinstance(N, int)):
            ax.plot(self.output[:,3]*N, label = 'S', color = '#003087')
            ax.plot(self.output[:,5]*N,  label = 'I',  color = 'red')
            ax.plot(N - ((self.output[:,5]*N)+(self.output[:,3]*N)), alpha = 0.5, label= 'R', color = '#33A02C')
            ax.set_ylabel('Number of Nodes')

        if log_scale:
            ax.set_yscale('log')

        plt.figtext(0.8, 0.01, caption, wrap=True, horizontalalignment='center', fontsize=12)
        plt.legend()
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
        
        fig = plt.figure(figsize = figsize, dpi = 200)
        ax = plt.subplot(ylim = [-0.05, 1.05])
        ax.plot(1 - (self.output[:,5]+self.output[:,3]) + self.output[:,5], 
                alpha = 0.5, 
                c = color,
                label= label, 
                ls = linestyle, linewidth = 2)
        # ax.legend()
        ax.set_title(title)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.show()
        
    def full_simulation(self, title: str = '', figsize:tuple = (12,5), log_scale:bool = False):
        fig = plt.figure(figsize = figsize, dpi = 200)
        ax = plt.subplot(ylim = [-0.05, 1.05])
        ax.plot(self.output[:,0], alpha =0.5, label = 'Fraction degree 1 nodes sus') # change of theta
        ax.plot(self.output[:,1], label = 'Prob Sus ego to infectious alter',
                )#change of p_infec 
        ax.plot(self.output[:,2], label = 'Prob Sus ego to Sus alter')# change of p_suscep 
        ax.plot(self.output[:,3], label = 'Frac S',color = '#003087', ls = '--') #proportion of S
        ax.plot(self.output[:,4], label = 'Infectious ego with an alter of any state')# change of M_I 
        ax.plot(self.output[:,5], alpha = 0.5, label = 'Frac I',  color = 'red',ls = '--') # change of I
        # recovered
        ax.plot(1 - (self.output[:,5]+self.output[:,3]), alpha = 0.5, label= 'Frac R', color = '#33A02C',ls = '--')
        ax.plot(1 - (self.output[:,5]+self.output[:,3]) + self.output[:,5], alpha = 0.5, c = 'black',label= 'CS Incidence', ls = ':')
        ax.legend(bbox_to_anchor = (1.1,0.8))
        ax.set_title(title)
        ax.set_ylabel('Proportion')
        ax.set_xlabel('Time Step')
        if log_scale:
            ax.set_yscale('log')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.show()
        
        
class SRResults(SimResults):
    
    def SIR_graph(self,  N:int = None, title:str = '', figsize:tuple = (12,5), log_scale:bool = False):
        fig = plt.figure(figsize = figsize, dpi = 200)
        ax = plt.subplot(ylim = [-0.05, 1.05])
        if (N == None):
            ax.plot(self.output[:,3], label = 'S',color = '#003087')
            ax.plot(self.output[:,4],  label = 'I',   color = 'red')
            ax.plot(1 - (self.output[:,4]+self.output[:,3]), alpha = 0.5, label= 'R', color = '#33A02C')
            ax.set_ylabel('Proportion of Nodes')

        elif (isinstance(N, int)):
            ax.plot(self.output[:,3]*N, label = 'S',color = '#003087')
            ax.plot(self.output[:,5]*N,  label = 'I',   color = 'red')
            ax.plot(N - ((self.output[:,5]*N)+(self.output[:,3]*N)), alpha = 0.5, label= 'R', color = '#33A02C')
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
        fig = plt.figure(figsize = figsize, dpi = 200)
        ax = plt.subplot(ylim = [-0.05, 1.05])
        ax.plot(1 - (self.output[:,4]+self.output[:,3]) + self.output[:,4], 
                alpha = 0.5, 
                c = color,
                label= label, 
                ls = linestyle)
        ax.legend()
        ax.set_title(title)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        plt.show()
        
    def full_simulation(self, title: str = '', figsize:tuple = (12,5), log_scale:bool = False):
        fig = plt.figure(figsize = figsize, dpi = 200)
        ax = plt.subplot(ylim = [-0.05, 1.05])

        ax.plot(self.output[:,0], label = r'$\theta$')
        ax.plot(self.output[:,1], label = 'pi')
        ax.plot(self.output[:,2], label = 'ps')
        ax.plot(self.output[:,3], label = 'S', ls = '--', color = '#003087')
        ax.plot(self.output[:,4],  label = 'I', ls = '--',   color = 'red')
        ax.plot(1 - (self.output[:,4]+self.output[:,3]), alpha = 0.5, label= 'R', ls = '--', color = '#33A02C')
        ax.set_ylabel('Proportion of Nodes')
        if log_scale:
            ax.set_yscale('log')
        plt.legend()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        plt.show()
    
    