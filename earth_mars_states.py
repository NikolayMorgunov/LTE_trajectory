import numpy as np
import kiam


def earth_mars_positions(jd0, jd1):
    T = jd1 - jd0
    N_int = 500
    dt = T / N_int

    earth_states = []
    mars_states = []
    for i in range(N_int):
        earth_states.append(kiam.planet_state(jd0 + dt * i, 'Sun', 'Earth'))
        mars_states.append(kiam.planet_state(jd0 + dt * i, 'Sun', 'Mars'))


    earth_states = np.array(earth_states, dtype='float32')
    mars_states = np.array(mars_states[-150:], dtype='float32')

    return earth_states, mars_states
