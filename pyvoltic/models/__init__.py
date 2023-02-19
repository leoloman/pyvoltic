"""
The :mod:`pyvoltic.models` module provides models to spread disease on a hetergenous network
"""
from ._classic_models import SIRNE, SIRSR
from ._ebcm import EBCM, MFSHEBCM, DynamicFixedDegree
from ._ext_models import SEIRSR
__all__ = ["SIRNE", 
           "SIRSR",
           "EBCM",
           "MFSHEBCM",
           "DynamicFixedDegree",
           "SEIRSR"
          ]