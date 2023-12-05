import time

from icecream import ic

from Algorithms.Algorithm import SortingAlgorithm


class MergeSort(SortingAlgorithm):
    def merge(self, lb, mid, ub):
        new = []
        i = lb
        j = mid + 1

        while i <= mid and j <= ub:
            if self.array[i] < self.array[j]:
                new.append(self.array[i])
                i += 1
            else:
                new.append(self.array[j])
                j += 1

        if i > mid:
            while j <= ub:
                new.append(self.array[j])
                j += 1
        else:
            while i <= mid:
                new.append(self.array[i])
                i += 1

        for i, val in enumerate(new):
            self.array[lb + i] = val
            # Yield a copy of the current state of the array for visualization
            yield list(self.array)

    def merge_sort(self, lb, ub):
        if ub > lb:
            mid = (lb + ub) // 2
            yield from self.merge_sort(lb, mid)
            yield from self.merge_sort(mid + 1, ub)
            yield from self.merge(lb, mid, ub)

    def sort(self):
        start_time = time.time()
        yield from self.merge_sort(0, len(self.array) - 1)
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time
        ic(f"Time taken: {elapsed_time} seconds")
