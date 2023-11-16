import random
from icecream import ic
import matplotlib.pyplot as plt
import matplotlib.animation as anim


class SortVisualizer:
    def __init__(self, sorting_algorithm):
        self.sorting_algorithm = sorting_algorithm
        self.array = sorting_algorithm.array

        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, len(self.array))
        self.ax.set_ylim(0, int(len(self.array) * 1.1))

        self.title = None
        self.bar_rec = None
        self.text = None
        self.epochs = [0]

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def update_plot(self, frame, rects):
        for rec, val in zip(rects, frame):
            rec.set_height(val)
        self.epochs[0] += 1
        self.text.set_text("No. of operations: {}".format(self.epochs[0]))

    def visualize(self):
        self.title = f"Sorting Algorithm Visualization: {
            type(self.sorting_algorithm).__name__}"
        self.bar_rec = self.ax.bar(
            range(len(self.array)), self.array, align='edge')
        self.ax.set_title(self.title)
        self.text = self.ax.text(0.02, 0.95, "", transform=self.ax.transAxes)

        algo_generator = self.sorting_algorithm.sort()
        # Adjust the interval to slow down the animation
        anima = anim.FuncAnimation(
            self.fig, func=self.update_plot, frames=algo_generator, fargs=(self.bar_rec,), interval=0, repeat=False, cache_frame_data=False
        )
        plt.show(block=False) # Adjust the duration as needed
        plt.close(self.fig)  # Close the figure after a specified duration
        ic(self.text)
