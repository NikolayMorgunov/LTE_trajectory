import numpy as np
import numpy.linalg as LA
import kiam
import random


def zero_point(N, jd0, jd1):
    T = jd1 - jd0

    dt = T / N

    F = np.array([0. for i in range(3 * N)], dtype='float32')
    # F = np.array([])

    for i in range(N):
        v_e = kiam.planet_state(jd0 + dt * i, 'Sun', 'Earth')[3:]
        if i < N:
            F[i * 3:(i + 1) * 3] = v_e / LA.norm(v_e) * 0.007
        else:
            F[i * 3:(i + 1) * 3] = -v_e / LA.norm(v_e) * 0
    return F
