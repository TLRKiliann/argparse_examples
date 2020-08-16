#!/usr/bin/python3
# -*- encoding:utf-8 -*-


"""
Use :
python3 arg_ex4.py 4
python3 arg_ex4.py 4 --verbose
python3 arg_ex4.py --verbose 4

"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print("the square of {} equals {}".format(args.square, answer))
else:
    print(answer)