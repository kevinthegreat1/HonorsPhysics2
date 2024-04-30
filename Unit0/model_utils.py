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


def graph(data: list[tuple[any, any, str]], y_name: str, y_units: str, x_name: str = "Time", x_units: str = "s", name_prefix: str = "", name_suffix: str = "", type: str = None, directory: str = None):
    for times, data, label in data:
        if type is None:
            plt.plot(times, data, label=f"{label}")
        else:
            plt.plot(times, data, type, label=f"{label}")
    x_label = f"{x_name} ({x_units})" if x_units else x_name
    y_label = f"{y_name} ({y_units})" if y_units else y_name
    plt.title(f"{name_prefix} {y_label} vs {x_label} {name_suffix}")
    plt.xlabel(f"{x_label}")
    plt.ylabel(f"{y_label}")
    plt.legend()
    if directory is not None:
        plt.savefig(f"{directory}.png", dpi=300, bbox_inches='tight')
    plt.show()
