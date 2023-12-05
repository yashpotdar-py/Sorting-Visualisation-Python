import time

from icecream import ic

from Algorithms.Algorithm import SortingAlgorithm


class BubbleSort(SortingAlgorithm):

    def sort(self):
        start_time = time.time()
        for x in range(self.n):
            for y in range(self.n - 1 - x):
                if self.array[y] > self.array[y + 1]:
                    self.array[y], self.array[y +
                                              1] = self.array[y + 1], self.array[y]
                    yield self.array

        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time
        ic(f"Time taken: {elapsed_time} seconds")
