import numpy as np
import pytest

from pyvoltic.models import EBCM, MFSHEBCM, SEIRSR, SIRNE, SIRSR
from pyvoltic.probability_generating_functions import (
    poisson_calc_g,
    poisson_calc_g1,
    poisson_calc_g2,
)

model_param_list = [
    (SIRNE, dict(r=0.2, mu=0.2, rho=0.2, epsilon=0.0001, timesteps=10)),
    (SIRSR, dict(r=0.2, mu=0.2, epsilon=0.0001, timesteps=10)),
    (SEIRSR, dict(r=0.8, a=0.5, mu=1, epsilon=0.0001, timesteps=10)),
    # check both methods of passing epsilon
    (SEIRSR, dict(r=0.8, a=0.5, mu=1, epsilon=(0.0001, 0.0002), timesteps=10)),
    (EBCM, dict(beta=0.2, gamma=0.2, epsilon=0.0001, timesteps=10)),
    (MFSHEBCM, dict(beta=0.2, gamma=0.2, epsilon=0.0001, timesteps=10)),
]


@pytest.mark.parametrize("model, model_params", model_param_list)
def test_model(model, model_params):
    model_obj = model(
        poisson_calc_g, poisson_calc_g1, poisson_calc_g2, probability_lambda=3
    )
    model_out = model_obj.run_simulation(**model_params)
    # ensure output is a numpy ndarray
    assert isinstance(model_out.output, np.ndarray)
    # ensure no negative values
    assert np.min(model_out.output) >= 0
