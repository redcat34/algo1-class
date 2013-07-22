#!/usr/bin/env python

def quicksort(list, choose_pivot = lambda l, *_ : l[0]):
    # helper function to do recursion without exposing "limit" parameters
    # (left and right), and comparison counter
    def _quicksort(left, right, comparisons):
        if left >= right:
            return comparisons

        pivot   = choose_pivot(list, left, right)
        middle  = partition(list, left, right)

        counter = comparisons + right - left
        counter = _quicksort(left, middle - 1, counter)
        counter = _quicksort(middle + 1, right, counter)
        return counter

    return _quicksort(0, len(list) - 1, 0)

def partition(list, left, right):
    pivot = list[left]
    i = left + 1
    for j in range(left + 1, right + 1):
        if list[j] < pivot:
            list[i], list[j] = list[j], list[i]
            i += 1
    list[left], list[i - 1] = list[i - 1], list[left]
    return i - 1

def last_pivot(list, first, last):
    list[first], list[last] = list[last], list[first]
    return list[first]

def median_pivot(list, first, last):
    # is x a median of x y and z?
    def is_median(x, y, z):
        return (x < y and x > z) or (x > y and x < z)

    middle = first + (last - first) // 2
    if is_median(list[middle], list[first], list[last]):
        list[first], list[middle] = list[middle], list[first]
    elif is_median(list[last], list[middle], list[first]):
        list[first], list[last] = list[last], list[first]

    return list[first]

def read_integer_file(path):
    return [int(s) for s in open(path).readlines()]

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help = "the integer file", type = str)
    parser.add_argument("-p", "--pivot", help = "pivot mode to use", \
            default = "first", choices = ["first", "last", "median"])
    parser.add_argument("-s", "--sort", help = "print the sorted file", \
            action = "store_true")
    args = parser.parse_args()

    numbers = read_integer_file(args.file)

    if args.pivot == "first":
        comparisons = quicksort(numbers)
    elif args.pivot == "last":
        comparisons = quicksort(numbers, last_pivot)
    elif args.pivot == "median":
        comparisons = quicksort(numbers, median_pivot)

    print("Number of comparisons made:", comparisons)
    if args.sort:
        print("Sorted list:", numbers)
