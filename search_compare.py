import randon
import time

def sequential_search(a_list, item):
  start = time.perf_counter()
  pos = 0
  found = False
  while pos < len(a_list) and not found:
    if a_list[pos] == item:
      found = True
    else:
      pos += 1
  elapsed = time.perf_counter() - start
  return found, elapsed

def ordered_sequential_search(a_list, itme):
  start = time.perf_counter()
  pos = 0
  found = False
  stop = False
  while pos < len(a_list) and not found and not stop:
    if a_list[pos] == item:
      found = True
    else:
        if a_list[pos] > item:
            stop = True
        else:
            pos += 1
  elapsed = time.perf_counter() - start
  return found, elapsed

def binary_search_interative(a_list, item):
  start = time.perf_counter()
  first = 0
  last = len(a_list) - 1
  found = False
  while first <= last and not found:
      mid = (first + last) // 2
      if a_list[mid] == item:
          found = True
      else:
          if item < a_list[mid]:
              last = mid - 1
          else:
              first = mid + 1
  elapsed = time.perf_counter() - start
  return found, elapsed

def binary_search_recursive(a_list, item):
  start = time.perf_counter()
  found = _binary_search_recursive_core(a_list, item, 0, len(a_list) - 1)
  elapsed = time.perf_counter() - start
  return found, elapsed

def _binary_search_recursive_core(a_list, item, first, last):
    if first > last:
        return False
    mid = (first + last) // 2
    if a_list[mid] == item:
        return True
    if item < a_list[mid]:
        return _binary_search_recursive_core(a_list, item, first, mid - 1)
    else:
        return _binary_search_recursive_core(a_list, item, mid + 1, last)

def _random_list(n):
    return [random.randint(1, 1_000_000) for _ in range(n)]

def _avg(values):
    return sum(values) / len(values)

def main():
    TARGET = 99_999_999
    TRIALS = 100
    SIZES = [500, 1000, 5000]

    for n in SIZES:
        times_seq, times_ord, times_bin_it, times_bin_rec = [], [], [], []
        for _ in range(TRIALS):
            1st = _random_list(n)
            _, t = sequential_search(1st, TARGET)
            times_seq.append(t)

            sorted_1st = sorted(1st)
            _, t = ordered_sequential_search(sorted_1st, TARGET)
            times_ord.append(t)
            _, t = binary_search_iterative(sorted_1st, TARGET)
            times_bin_it.append(t)
            _, t = binary_search_recursive(sorted_1st, TARGET)
            times_bin_rec.append(t)

        print(f"List size {n}")
        print(f"Sequential Search took {_avg(times_seq):10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {_avg(times_ord):10.7f} seconds to run, on average")
        print(f"Binary Search Iterative took {_avg(times_bin_it):10.7f} seconds to run, on average")
        print(f"Binary Search Recursive took {_avg(times_bin_rec):10.7f} seconds to run, on average")
        print("")

if __name__ == "__main__":
    main()
