import numpy as np
import numpy.linalg as LA
import non_dim


def relay(F, F_max):
    F_max = non_dim.is_to_nd('f', F_max)
    f = []
    for i in np.reshape(F, (-1, 3)):
        if LA.norm(i) < 0.5 * F_max:
            f.append(i * 0)
        else:
            f.append(i / LA.norm(i) * F_max)

    f = np.array(f)

    return f

