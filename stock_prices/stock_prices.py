#!/usr/bin/python

import argparse


def find_max_profit(prices):
    maxProfit = 0

    index = 0

    while index < len(prices):
        if index == 0:
            maxProfit = prices[index] - prices[index + 1]
        for i in range(index, len(prices) - 1):
            difference = prices[index] - prices[i + 1]  # negative
            if difference < maxProfit:
                maxProfit = difference
        index += 1
    # Need to flip the sign for the correct profit/deficit
    return maxProfit * -1


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
