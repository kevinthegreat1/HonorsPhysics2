import numpy as np
import matplotlib.pyplot as plt


def euler_method(acceleration_function: callable, start_time: float = 0, end_time: float = 10, steps: int = 1000, times=None, position_initial: float = 0, velocity_initial: float = 0, acceleration_initial: float = 0):
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


def graph(name: str, units: str, data: list[tuple[any, any, str]], directory: str = None):
    for times, data, label in data:
        plt.plot(times, data, label=f"{label} {name}")
    plt.title(f"{name} vs Time")
    plt.xlabel('Time (s)')
    plt.ylabel(f"{name} ({units})")
    plt.legend()
    if directory is not None:
        plt.savefig(f"{directory}.png", dpi=300)
    plt.show()
