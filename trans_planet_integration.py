import numpy as np
from right_part import right_part
import non_dim

def trans_planet_integration(rv0, m0, Ig, F, dt_F, N_int, dt_int):
    rvm = np.concatenate([np.copy(rv0), np.array([m0])])

    craft_states = [np.copy(rvm)]

    # F = non_dim.is_to_nd('f', F)
    F = np.copy(np.reshape(F, (-1, 3)))


    for i in range(N_int):
        cur_t = i * dt_int
        f = F[int(cur_t / dt_F)]

        # Рунге-Кутт 4 порядка
        k1 = right_part(rvm, f, Ig)
        k2 = right_part(rvm + dt_int * k1 / 2, f, Ig)
        k3 = right_part(rvm + dt_int * k2 / 2, f, Ig)
        k4 = right_part(rvm + dt_int * k3, f, Ig)

        rvm += dt_int / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

        craft_states.append(np.copy(rvm))

    return np.array(craft_states)
