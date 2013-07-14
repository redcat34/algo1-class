#!/usr/bin/env python

def sort_and_count(lst):
    if len(lst) <= 1:
        return (lst, 0)
    (left,  left_count)  = sort_and_count(lst[ : len(lst) // 2])
    (right, right_count) = sort_and_count(lst[len(lst) // 2 : ])
    (total, split_count) = merge_and_count_split(left, right)
    return (total, left_count + right_count + split_count)

def merge_and_count_split(left, right):
    merged = [ ]
    counter, i, j = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            counter += len(left[i:])
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return (merged, counter)

def read_integer_file(path):
    return [int(s) for s in open(path).readlines()]

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help = "the integer file", type = str)
    parser.add_argument("-s", "--sort", help = "print the sorted file", action = "store_true")
    args = parser.parse_args()

    numbers = read_integer_file(args.file)
    (sorted_list, inversions) = sort_and_count(numbers)

    print("Number of inversions found:", inversions)
    if args.sort:
        print("Sorted list:", sorted_list)
