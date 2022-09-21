import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class CGOL:
    def __init__(self, size):

        self.world = np.zeros((size + 2, size + 2))
        self.add_glider_gun()
        self.history = [np.copy(self.world)]

    def add_glider_gun(self):
        for i in range(self.world.shape[0]):
            for j in range(self.world.shape[1]):
                if (i, j) in [
                    (1, 24),
                    (2, 22),
                    (2, 24),
                    (3, 13),
                    (3, 21),
                    (3, 23),
                    (3, 35),
                    (3, 36),
                    (4, 12),
                    (4, 13),
                    (4, 20),
                    (4, 23),
                    (4, 35),
                    (4, 36),
                    (5, 1),
                    (5, 2),
                    (5, 11),
                    (5, 12),
                    (5, 17),
                    (5, 18),
                    (5, 21),
                    (5, 23),
                    (6, 1),
                    (6, 2),
                    (6, 10),
                    (6, 11),
                    (6, 12),
                    (6, 17),
                    (6, 18),
                    (6, 22),
                    (6, 24),
                    (7, 11),
                    (7, 12),
                    (7, 17),
                    (7, 18),
                    (7, 24),
                    (8, 12),
                    (8, 13),
                    (9, 13),
                ]:
                    self.world[i, j] = 1

    def next_cell_state(self, neigh):

        total = np.sum(neigh)
        count = total - neigh[1, 1]

        if neigh[1, 1] == 1:
            if count == 2 or count == 3:
                return 1
            else:
                return 0
        else:
            if count == 3:
                return 1
            else:
                return 0

    def get_next_state(self):
        world_copy = np.copy(self.world)
        for (i, j), value in np.ndenumerate(world_copy):
            if (
                i == 0
                or i == world_copy.shape[0] - 1
                or j == 0
                or j == world_copy.shape[1] - 1
            ):
                continue
            neigh = np.array(
                [
                    world_copy[i - 1, j - 1 : j + 2],
                    world_copy[i, j - 1 : j + 2],
                    world_copy[i + 1, j - 1 : j + 2],
                ]
            )
            self.world[i, j] = self.next_cell_state(neigh)

    def animate_world(self):
        for _ in range(200):
            self.get_next_state()
            self.history.append(np.copy(self.world))

        matplotlib.rcParams["toolbar"] = "None"
        fig = plt.figure()
        im = plt.imshow(self.history[0], animated=True)

        def updateFig(frame):
            im.set_array(frame)

        ani = animation.FuncAnimation(fig, updateFig, frames=self.history)
        plt.axis("off")
        plt.grid(visible=True, which="minor")
        plt.show()


if __name__ == "__main__":
    cgol = CGOL(40)
    cgol.animate_world()
