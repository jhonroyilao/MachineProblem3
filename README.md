# Machine Problem 3 : Decrease and Conquer Limitations

This project explores the limitations of several classic **Decrease and Conquer** algorithms by implementing and analyzing them using python.

## 📌Covered Algorithms

- Binary Search
- Russian Peasant Multiplication
- Insertion Sort
- Josephus Problem

## 💭Limitations Demonstrated

### 1. Binary Search
- Only works on **sorted arrays**.
- Fails or gives incorrect results when applied to unsorted data.
- Requires **random-access data structures** like arrays (inefficient on linked lists).

### 2. Russian Peasant Multiplication
- Only works properly for **positive integers**.
- Fails or behaves unexpectedly with **negative numbers** or **floating-point values**.
- Not commonly used in real-world applications due to inefficiency.

### 3. Insertion Sort
- Worst-case time complexity is **O(n²)**, making it inefficient on **large or reverse-sorted datasets**.
- Suitable only for **small datasets** or nearly sorted arrays.

### 4. Josephus Problem
- Naive implementations have **poor time complexity** (recursive or iterative with full simulation).
- Can be **confusing to implement** for non-standard step sizes.
- Not practical for real-time or large-scale simulations without optimization (e.g., using mathematical formulas).

## 📁 Contents

- `binary_search_limitation.py`
- `russian_peasant_limitation.py`
- `insertion_sort_limitation.py`
- `josephus_limitation.py`

Each file demonstrates a limitation of its respective algorithm.


