"""
The :mod:`pyvoltic.vizualisations` module provides a series of functions to compare cumulative incidence across simulation runs, and other useful viz
"""
from ._viz_functions import (NE_multi_cumulative_incidence, 
                             SR_multi_cumulative_incidence,
                             EBCM_multi_cumulative_incidence)

__all__ = ["NE_multi_cumulative_incidence", 
           "SR_multi_cumulative_incidence",
          "EBCM_multi_cumulative_incidence"]

