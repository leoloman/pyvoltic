"""
The :mod:`pyvoltic.results` module provides the model results classes for when an output of a simulation is run. Each class provides basic plotting functions and basic information about the simulation parameters
"""
from ._simulation_results import EBCMResults, DFDResults, NEResults, SRResults, SEIRSRResults

__all__ = ["EBCMResults", "DFDResults", "NEResults", "SRResults", "SEIRSRResults"]