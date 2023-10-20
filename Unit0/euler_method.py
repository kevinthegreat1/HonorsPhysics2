import numpy as np


def compute(acceleration_function, start_time: float = 0, end_time: float = 10, steps: int = 1000, times=None, position_initial: float = 0, velocity_initial: float = 0, acceleration_initial: float = 0):
    if times is None:
        times = np.linspace(start_time, end_time, steps)
    positions = [position_initial]
    velocities = [velocity_initial]
    accelerations = [acceleration_initial]
    for i in range(len(times) - 1):
        accelerations.append(acceleration_function(times[i + 1], positions[-1], velocities[-1], accelerations[-1]))
        velocities.append(velocities[-1] + accelerations[-1] * (times[i + 1] - times[i]))
        positions.append(positions[-1] + velocities[-1] * (times[i + 1] - times[i]))
    return times, positions, velocities, accelerations
