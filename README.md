# Sorting Visualization

This project provides a visual representation of various sorting algorithms using Matplotlib in Python.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Algorithms](#algorithms)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project visualizes several sorting algorithms to help understand their operations step by step. It includes a visualizer module using Matplotlib and various sorting algorithms implemented in an object-oriented manner.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/yashpotdar-py/Sorting-Visualisation-Python.git
    ```

2. Navigate to the project directory:

    ```
    cd sorting-visualization
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the `main-script.py` file:

    ```
    python main-script.py
    ```

2. Enter the number of elements and choose the sorting algorithm when prompted.

3. Watch the visualization of the selected sorting algorithm.

## Folder Structure

```
├── Algorithms
│   ├── BubbleSort.py
│   ├── InsertionSort.py
│   ├── QuickSort.py
│   ├── SelectionSort.py
│   ├── MergeSort.py
│   ├── HeapSort.py
│   ├── ShellSort.py
│   ├── CountSort.py
├── Visualizer
│   ├── __init__.py
│   ├── visualizer.py
├── main-script.py
├── requirements.txt
├── README.md
```

- `Algorithms`: Contains individual files for each sorting algorithm.
- `Visualizer`: Contains the visualizer module.
- `main-script.py`: Main script to run the visualization.
- `requirements.txt`: Dependencies for the project.

## Algorithms

The `Algorithms` folder contains implementations of the following sorting algorithms:

1. Bubble Sort
2. Insertion Sort
3. Quick Sort
4. Selection Sort
5. Merge Sort
6. Heap Sort
7. Shell Sort
8. Count Sort

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
