from trans_planet_integration import trans_planet_integration
from zero_point import zero_point
import non_dim
import numpy as np


def test(jd0, jd1, m0, Ig, rv0):
    N_F = 40
    N_int = 300

    F = zero_point(N_F, jd0, jd1)
    F = non_dim.is_to_nd('f', F)

    Ig = non_dim.is_to_nd('Ig', Ig)
    rv0 = non_dim.is_to_nd('rv', rv0)

    T = non_dim.is_to_nd('t', (jd1 - jd0))

    craft_states = trans_planet_integration(rv0, m0, Ig, F, T / N_F, N_int, T / N_int)
    craft_states = non_dim.nd_to_is('rv_s', craft_states)

    return non_dim.nd_to_is('f', F), craft_states
