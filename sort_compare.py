import random
import time

def insertion_sort(a_list):
    work = list(a_list)
    start = time.perf_counter()
    for index in range(1, len(work)):
        current_value = work[index]
        position = index
        while position > 0 and work[position - 1] > current_value:
            work[position] = work[position - 1]
            position -= 1
        work[position] = current_value
    elapsed = time.perf_counter() - start
    return work, elapsed

def shell_sort(a_list):
    work = list(a_list)
    start = time.perf_counter()
    gap = len(work) // 2
    while gap > 0:
        for i in range(gap, len(work)):
            current_value = work[i]
            position = i
            while position >= gap and work[position - gap] > current_value:
                work[position] = work[position - gap]
                position -= gap
            work[position] = current_value
        gap //= 2
    elapsed = time.perf_counter() - start
    return work, elapsed

def python_sort(a_list):
    work = list(a_list)
    start = time.perf_counter()
    work.sort()
    elapsed = time.perf_counter() - start
    return work, elapsed

def _random_list(n):
    return [random.randint(1, 1_000_000) for _ in range(n)]

def _avg(values):
    return sum(values) / len(values)

def main():
    TRIALS = 100
    SIZES = [500, 1000, 5000]

    for n in SIZES:
        times_ins, times_shell, times_py = [], [], []
        for _ in range(TRIALS):
            lst = _random_list(n)
            _, t = insertion_sort(lst)
            times_ins.append(t)
            _, t = shell_sort(lst)
            times_shell.append(t)
            _, t = python_sort(lst)
            times_py.append(t)

    print(f"List size {n}")
    print(f"Insertion Sort took {_avg(times_ins):10.7f} seconds to run, on average")
    print(f"Shell Sort took {_avg(times_shell):10.7f} seconds to run, on average")
    print(f"Python Sort took {_avg(times_py):10.7f} seconds to run, on average")
    print("")

if __name__ == "__main__":
    main()
