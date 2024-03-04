from random import choice

class RandomWalk():
    """a class to generate random walk data"""
    def __init__(self, num_points=5000):
        """initialize properties of random walk"""
        self.num_points = num_points

        # all random walks are start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calculate all points included in random walks"""

        # keep random walk, until the list reaches the specified length
        while len(self.x_values) < self.num_points:
            # decide the direction to move forward and the distance to move forward in this direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # refused to step in place
            if x_step == 0 and y_step == 0:
                continue

            # calculate the values of x and y for the next point
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
