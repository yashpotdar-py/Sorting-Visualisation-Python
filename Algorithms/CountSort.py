from Algorithms.Algorithm import SortingAlgorithm
from icecream import ic
import time


class CountSort(SortingAlgorithm):
    def sort(self):
        start_time = time.time() 

        max_val = max(self.array) + 1
        count = [0] * max_val

        for num in self.array:
            count[num] += 1
            # Yield a copy of the current state of the array for visualization
            yield list(self.array)

        i = 0
        for num in range(max_val):
            for _ in range(count[num]):
                self.array[i] = num
                i += 1
                # Yield a copy of the current state of the array for visualization
                yield list(self.array)

        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time
        ic(f"Time taken: {elapsed_time} seconds")
