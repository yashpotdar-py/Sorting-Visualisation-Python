import time

from icecream import ic

from Algorithms.Algorithm import SortingAlgorithm


class QuickSort(SortingAlgorithm):
    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def partition(self, low, high):
        pivot = self.array[high]
        i = low - 1

        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1
                self.swap(i, j)
                # Yield a copy of the current state of the array for visualization
                yield list(self.array)

        self.swap(i + 1, high)
        # Yield a copy of the current state of the array for visualization
        yield list(self.array)
        return i + 1

    def quick_sort(self, low, high):
        if low < high:
            pi = yield from self.partition(low, high)

            yield from self.quick_sort(low, pi - 1)
            yield from self.quick_sort(pi + 1, high)

    def sort(self):
        start_time = time.time()
        yield from self.quick_sort(0, len(self.array) - 1)
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time
        ic(f"Time taken: {elapsed_time} seconds")
