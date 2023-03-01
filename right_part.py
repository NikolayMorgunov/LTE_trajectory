import numpy as np
import kiam
from numpy import linalg as LA


def right_part(rvm, f, Ig):

    r = rvm[:3]
    v = rvm[3:6]
    m = rvm[6]


    abs_r = LA.norm(r)
    abs_f = LA.norm(f)

    dr_dt = v
    dv_dt = -r / abs_r ** 3 + f / m
    abs_a = LA.norm(dv_dt)

    dm_dt = -abs_f / Ig

    drvm_dt = np.concatenate([dr_dt, dv_dt, np.array([dm_dt])])
    return drvm_dt
