import matplotlib.pyplot as plt

from random_walk import RandomWalk

# create a instance of RandomWalk, and draw all points it contains
# rw = RandomWalk()
# rw.fill_walk()
#
# plt.scatter(rw.x_values, rw.y_values, s=15)
# plt.show()

#######################

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.figure(figsize=(10, 10))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=15)

    # highlight the starting point and ending point
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # hide coordinate axis
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("make another walk? (y/n): ")
    if keep_running == "n":
        break
