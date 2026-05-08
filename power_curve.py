import matplotlib.pyplot as plt

def show_plot(duration, data):
    plt.plot(duration, data)
    plt.xlabel('Duration')
    plt.ylabel('Power (W)')
    plt.title('Power Curve')
    plt.grid()
    plt.savefig('power_curve.png')  
    plt.show()
    