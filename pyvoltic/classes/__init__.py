"""
The :mod:`pyvoltic.classes` module parent classes for the models and the simulation results to inherit from
"""
from ._sim_results import SimResults
from ._volz_framework import VolzFramework

__all__ = ["SimResults", 
    "VolzFramework", 
]