"""
The :mod:`pyvoltic.probability_generating_functions` module implements a variety of probabiltiy generating functions, with a poisson, powerlaw and network based funcitons ready to go
"""

from ._poisson_pgf import poisson_calc_g, poisson_calc_g1, poisson_calc_g2
from ._powerlaw_pgf import (
    powerlaw_calc_g,
    powerlaw_calc_g1,
    powerlaw_calc_g2,
    powerlaw_p_vec,
)
from ._probability_generating_function import (
    get_PGF,
    get_PGF_first_derivate,
    get_PGF_second_derivate,
    get_Pk,
)

__all__ = [
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
    "get_PGF_second_derivate",
]
