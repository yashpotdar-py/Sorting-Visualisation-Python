from Algorithms.Algorithm import SortingAlgorithm
from icecream import ic
import time


class InsertionSort(SortingAlgorithm):
    def sort(self):
        start_time = time.time()

        for x in range(1, self.n):
            key = self.array[x]
            y = x - 1

            while y >= 0 and key < self.array[y]:
                self.array[y], self.array[y +
                                          1] = self.array[y+1], self.array[y]
                y -= 1

            self.array[y+1] = key
            yield self.array

        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time
        ic(f"Time taken: {elapsed_time} seconds")
