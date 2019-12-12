#!/usr/bin/python

import sys
import itertools


def rock_paper_scissors(n):
    moves = ['rock', 'paper', 'scissors']
    outcomes = []
    perm = itertools.product(moves, repeat=n)
    # n is the number of rounds
    for ways in perm:
        outcomes.append(list(ways))
    return outcomes


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
