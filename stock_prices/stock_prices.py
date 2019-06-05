#!/usr/bin/python

import argparse


def find_max_profit(prices):
    global_max = 0
    if len(prices) < 2:  # not enough elements to buy and sell
        return global_max

    i = 0
    while i < len(prices)-1:
        curr_price = prices[i]
        max_potential_price = max(prices[i+1:])
        if max_potential_price - curr_price > global_max:
            global_max = max_potential_price - curr_price
        i += 1
    return global_max


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
