import time

from icecream import ic

from Algorithms.Algorithm import SortingAlgorithm


class HeapSort(SortingAlgorithm):
    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.array[l] > self.array[largest]:
            largest = l

        if r < n and self.array[r] > self.array[largest]:
            largest = r

        if largest != i:
            self.swap(i, largest)
            # Yield a copy of the current state of the array for visualization
            yield list(self.array)
            yield from self.heapify(n, largest)

    def sort(self):
        start_time = time.time()
        n = len(self.array)

        for i in range(n // 2 - 1, -1, -1):
            yield from self.heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.swap(0, i)
            # Yield a copy of the current state of the array for visualization
            yield list(self.array)
            yield from self.heapify(i, 0)

        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time
        ic(f"Time taken: {elapsed_time} seconds")
