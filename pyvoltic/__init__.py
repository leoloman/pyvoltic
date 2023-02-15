
__import__("pkg_resources").declare_namespace(__name__)

__version__ = '0.0.1'

from models import SIRNE, SIRSR, EBCM

from probability_generating_functions import (poisson_calc_g, 
    poisson_calc_g1, 
    poisson_calc_g2,
    powerlaw_p_vec, 
    powerlaw_calc_g, 
    powerlaw_calc_g1, 
    powerlaw_calc_g2,
    get_Pk,
    get_PGF,
    get_PGF_first_derivate,
    get_PGF_second_derivate
)
                                              
                                              
__all__ = ["SIRNE", 
           "SIRSR", 
           "EBCM",
    "poisson_calc_g", 
    "poisson_calc_g1", 
    "poisson_calc_g2",
    "powerlaw_p_vec", 
    "powerlaw_calc_g", 
    "powerlaw_calc_g1", 
    "powerlaw_calc_g2",
    "get_Pk",
    "get_PGF",
    "get_PGF_first_derivate",
    "get_PGF_second_derivate"
]