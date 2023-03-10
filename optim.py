from scipy.optimize import minimize
import numpy as np
import numpy.linalg as LA
from trans_planet_integration import trans_planet_integration
from zero_point import zero_point
import non_dim
import relay


def f_to_min(F):
    res = 0
    N_F = int(F.size / 3)

    f = np.reshape(F, (-1, 3))

    for i in range(N_F):
        res += LA.norm(f[i]) ** 2
    return res / 40


def c(rv0, rv1, m0, Ig, F, dt_F, N_int, dt_int):
    final_point = trans_planet_integration(rv0, m0, Ig, F, dt_F, N_int, dt_int)[-1][:6]

    final_r = np.copy(final_point[:3])
    c_r = (np.copy(rv1[:3]) - final_r)

    final_v = np.copy(final_point[3:])
    c_v = (np.copy(rv1[3:]) - final_v)

    c = np.concatenate([c_r, c_v])

    return c


def callback(x, state):
    print(state.nit, LA.norm(state.constr), state.fun, LA.norm(state.lagrangian_grad), sep='\n')

    print()
    print()
    with open('cur_F.txt', 'w') as f:
        f.write(str(list(non_dim.nd_to_is('f', state.x))))


def optim(rv0, rv1, m0, Ig, jd0, jd1):
    T = non_dim.is_to_nd('t', (jd1 - jd0))
    N_F = 40
    N_int = 300
    dt_F = T / N_F
    dt_int = T / N_int

    F0 = zero_point(N_F, jd0, jd1)
    F0 = non_dim.is_to_nd('f', F0)

    Ig = non_dim.is_to_nd('Ig', Ig)
    rv0 = non_dim.is_to_nd('rv', rv0)
    rv1 = non_dim.is_to_nd('rv', rv1)

    cons = {'type': 'eq', 'fun': lambda x: c(rv0, rv1, m0, Ig, x, dt_F, N_int, dt_int)}

    F = minimize(lambda x: f_to_min(x), F0,
                 method='trust-constr',
                 constraints=cons,
                 callback=callback).x

    F = relay.relay(F, 0.014)
    craft_states = non_dim.nd_to_is('rv_s', trans_planet_integration(rv0, m0, Ig, F, dt_F, N_int, dt_int))

    F = non_dim.nd_to_is('f', F)
    return F, craft_states
