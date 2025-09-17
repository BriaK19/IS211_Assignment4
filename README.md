# IS211 – Assignment 4: Algorithm Benchmarking
__

This repo contains my solutions for **Week 4 Assignment** in IS211.
__

Files
- `search_compare.py` – compares **Sequential Search**, **Ordered Sequential Search**, **Binary Search (Iterative)**, and **Binary Search (Recursive)** in a *worst-case* scenario.
- `sort_compare.py` – compares **Insertion Sort**, **Shell Sort**, and Python’s built-in **Timsort** in an *average-case* scenario.
- `search_results.txt` – saved output from running `search_compare.py`.
- `sort_results.txt` – saved output from running `sort_compare.py`.
__

How to Run
Clone the repo and run each script with Python 3:

```bash
python3 search_compare.py
python3 sort_compare.py

The programs will:
Generate random lists of sizes 500, 1000, and 5000.
Run each algorithm 100 times per size.
Print the average runtime for each algorithm.

Example Output

When running each script, the results are grouped by list size.  
Here’s a sample of what the output looks like (for list size 500):
