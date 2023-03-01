import numpy as np
import kiam
from draw_trajectories import draw_trajectories
from earth_mars_states import earth_mars_positions
from optim import optim
from test import test

# начальная и конечная даты
jd0 = kiam.juliandate(2024, 3, 1, 0, 0, 0)
jd1 = kiam.juliandate(2025, 12, 1, 0, 0, 0)
T = jd1 - jd0  # сутки

# характеристики аппарата (СИ)
m0 = 140
I = 860
g = 9.81

Ig = I * g / 1000  # км/с

# сетка интегрирования
N_int = 300

earth_states, mars_states = earth_mars_positions(jd0, jd1)

F, craft_states = optim(np.copy(earth_states[0]), np.copy(mars_states[-1]), m0, Ig, jd0, jd1)
print(F)
# craft_states = test(jd0, jd1, m0, Ig, np.copy(earth_states[0]))

earth_states = np.transpose(earth_states)
mars_states = np.transpose(mars_states)

craft_states = np.transpose(craft_states)


draw_trajectories(earth_states, mars_states, craft_states)


print(craft_states[6])
