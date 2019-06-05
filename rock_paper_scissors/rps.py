#!/usr/bin/python

import sys
import math


def ternary(n, length):
    nums = []
    if n > 0:
        while n:
            n, r = divmod(n, 3)
            nums.append(str(r))
    while len(nums) < length:
        nums.append('0')
    return ['rock' if elem == '0' else 'paper' if elem == '1' else 'scissors' for elem in list(reversed(nums))]


def rock_paper_scissors(n):
    state = [0]*n
    results = []
    for x in range(3**n):
        results.append(ternary(x, n))
    return results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
