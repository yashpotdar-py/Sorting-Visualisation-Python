import time

from icecream import ic

from Algorithms.Algorithm import SortingAlgorithm


class ShellSort(SortingAlgorithm):
    def sort(self):
        start_time = time.time()
        n = len(self.array)
        sublist_count = n // 2

        while sublist_count > 0:
            for start_position in range(sublist_count):
                yield from self.gap_insertion_sort(start_position, sublist_count)

            sublist_count //= 2

        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time
        ic(f"Time taken: {elapsed_time} seconds")

    def gap_insertion_sort(self, start, gap):
        for i in range(start + gap, len(self.array), gap):
            current_value = self.array[i]
            position = i

            while position >= gap and self.array[position - gap] > current_value:
                self.array[position] = self.array[position - gap]
                position = position - gap
                # Yield a copy of the current state of the array for visualization
                yield list(self.array)

            self.array[position] = current_value
            # Yield a copy of the current state of the array for visualization
            yield list(self.array)
