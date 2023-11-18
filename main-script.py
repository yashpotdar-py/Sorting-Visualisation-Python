import random
from icecream import ic
import matplotlib.pyplot as pt
from Algorithms.BubbleSort import BubbleSort
from Algorithms.InsertionSort import InsertionSort
from Algorithms.QuickSort import QuickSort
from Algorithms.SelectionSort import SelectionSort
from Algorithms.MergeSort import MergeSort
from Algorithms.HeapSort import HeapSort
from Algorithms.ShellSort import ShellSort
from Algorithms.CountSort import CountSort
from Visualizer.visualizer import SortVisualizer


def create_random_array(n):
    array = [i + 1 for i in range(n)]
    random.shuffle(array)
    return array


def run_algorithm(algorithm, array):
    algo = algorithm(array)
    title = algorithm.__name__
    ic(title)

    visualizer = SortVisualizer(algo)
    visualizer.visualize()


if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    array = create_random_array(n)

    algorithms = [
        BubbleSort, InsertionSort, QuickSort, SelectionSort,
        MergeSort, HeapSort, ShellSort, CountSort
    ]

    for algorithm in algorithms:
        run_algorithm(algorithm, list(array))
