#!/usr/bin/env python

def read_integer_file(path):
    return [ int(n) for n in open(path).readlines() ]

def median_maintenance(intlist):
    from heapq import heappush, heappop

    integers = intlist[ : ]
    upper, lower = [ ], [ ]

    while integers:
        if not lower or integers[0] < -lower[0]:
            heappush(lower, -integers.pop(0))
        else:
            heappush(upper, integers.pop(0))

        diff = len(upper) - len(lower)
        if diff > 1:
            heappush(lower, -heappop(upper))
        elif diff < -1:
            heappush(upper, -heappop(lower))

        yield upper[0] if len(upper) > len(lower) else -lower[0]


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help = "the integer file", type = str)
    parser.add_argument("-m", "--modulo",
            help = "calculate the given modulo to the median sum", type = int)
    parser.add_argument("-p", "--print",
            help = "print found median", action = "store_true")
    args = parser.parse_args()

    integers = read_integer_file(args.file)
    medians  = list(median_maintenance(integers))
    med_sum  = sum(medians)

    if args.print:
        print("Final median:", medians[-1])

    print("Sum of all medians:", med_sum)

    if args.modulo:
        print("Modulo ", args.modulo, ": ", med_sum % args.modulo, sep = "")

