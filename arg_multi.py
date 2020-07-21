#!/usr/bin/python3
# -*- encoding:utf-8 -*-


import argparse


# * nargs expects 0 or more arguments

parser = argparse.ArgumentParser()
parser.add_argument('num', type=int, nargs='*')
args = parser.parse_args()

print(f"The sum of values is {sum(args.num)}")