#!/usr/bin/env python

def read_hash_file(path):
    return { int(x) : 0 for x in open(path).readlines() }

def count_two_sum(dictionary, low, high, show = False):
    count = 0
    for t in range(low, high + 1):
        for x in dictionary:
            y = t - x
            if y in dictionary and y is not x:
                count += 1
                if show:
                    print(count, ":", x, "+", y, "=", t)
                break
    return count

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help = "the integer file", type = str)
    parser.add_argument("low",  help = "lower limit for interval", type = int)
    parser.add_argument("high", help = "higher limit for interval", type = int)
    parser.add_argument("-s", "--show", help = "print found targets",
            action = "store_true")
    args = parser.parse_args()

    dictionary = read_hash_file(args.file)
    counter    = count_two_sum(dictionary, args.low, args.high, args.show)

    print("Number of target values in [", args.low, ",", args.high, "]:")
    print(counter)
