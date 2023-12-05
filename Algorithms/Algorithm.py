from icecream import ic


class SortingAlgorithm:
    def __init__(self, array) -> None:
        self.array = array
        self.n = len(array)

    def sort(self):
        ic(NotImplementedError)
        raise NotImplementedError("Sort method not yet Implemented")
