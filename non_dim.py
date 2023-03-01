import kiam
import numpy as np


def is_to_nd(type: str, a: np.array):
    units = kiam.units('sun', 'earth')
    b = np.copy(a)

    if type == 'rv_s':
        b = np.transpose(b)
        b[:3] = units['DistUnit']
        b[3:6] /= units['VelUnit']
        b = np.transpose(b)
    elif type == 't':
        b /= units['TimeUnit']
    elif type == 'f':
        b /= units['AccUnit']
    elif type == 'rv':
        b[:3] /= units['DistUnit']
        b[3:6] /= units['VelUnit']
    elif type == 'Ig':
        b /= units['VelUnit']

    return b


def nd_to_is(type: str, a: np.array):
    units = kiam.units('sun', 'earth')
    b = np.copy(a)

    if type == 'rv_s':
        b = np.transpose(b)
        b[:3] *= units['DistUnit']
        b[3:6] *= units['VelUnit']
        b = np.transpose(b)
    elif type == 't':
        b *= units['TimeUnit']
    elif type == 'f':
        b *= units['AccUnit']
    elif type == 'rv':
        b[:3] *= units['DistUnit']
        b[3:6] *= units['VelUnit']
    elif type == 'Ig':
        b *= units['VelUnit']

    return b