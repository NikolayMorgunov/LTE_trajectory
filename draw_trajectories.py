import kiam


def draw_trajectories(earth_states, mars_states, craft_states):
    fig = kiam.plot3(earth_states[0], earth_states[1], earth_states[2], name='Earth')
    fig = kiam.plot3(mars_states[0], mars_states[1], mars_states[2], fig=fig, name='Mars')
    fig = kiam.plot3(craft_states[0], craft_states[1], craft_states[2], fig=fig, name='Spasecraft')

    # fig = kiam.plot3(craft_states[0], craft_states[1], craft_states[2], name='Spasecraft trajectory')

    kiam.save_figure(fig, 'plot.html')
