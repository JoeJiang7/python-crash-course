import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values,  linewidth=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.show()

    while True:
        keep_running = input("Make another walk? (y/n): ")
        if keep_running == 'y' or keep_running == 'n':
            break

    if keep_running == 'n':
        break

