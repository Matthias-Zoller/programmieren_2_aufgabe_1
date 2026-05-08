from load_data import load_data
from sort import bubble_sort
from power_curve import show_plot
import numpy as np

if __name__ == "__main__":
    data = load_data('activity.csv')
    power_W = data['PowerOriginal']
    duration = data['Duration']
    print(power_W)
    sorted_power_W = bubble_sort(power_W)
    show_plot(np.arange(len(duration)), sorted_power_W)