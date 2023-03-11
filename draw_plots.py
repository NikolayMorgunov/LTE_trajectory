import kiam
import numpy as np
import numpy.linalg as LA


def draw_plots(earth_states, mars_states, craft_states, F):
    fig_traj = kiam.plot3(earth_states[0], earth_states[1], earth_states[2], name='Earth')
    fig_traj = kiam.plot3(mars_states[0], mars_states[1], mars_states[2], fig=fig_traj, name='Mars')
    fig_traj = kiam.plot3(craft_states[0], craft_states[1], craft_states[2], fig=fig_traj, name='Spasecraft')

    kiam.save_figure(fig_traj, 'trajectory.html')

    f = np.reshape(F, (-1, 3))
    f_abs = np.array([LA.norm(i) * 1e3 for i in f])
    n_s = np.linspace(0, f_abs.size - 1, f_abs.size)
    fig_thrust = kiam.plot(n_s, f_abs, xlabel='N', ylabel='F, 1e-3 Н')
    kiam.save_figure(fig_thrust, 'thrust_plot.html')
