from Algorithms.Algorithm import SortingAlgorithm
from icecream import ic
import time


class SelectionSort(SortingAlgorithm):
    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def sort(self):
        start_time = time.time()
        n = len(self.array)

        for i in range(n - 1):
            min_index = i

            for j in range(i + 1, n):
                if self.array[j] < self.array[min_index]:
                    min_index = j

            if min_index != i:
                self.swap(i, min_index)
                # Yield a copy of the current state of the array for visualization
                yield list(self.array)

        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time
        ic(f"Time taken: {elapsed_time} seconds")
