#!/usr/bin/python3
# -*- encoding:utf-8 -*-


"""
Use :
python3 arg_ex2.py 4
python3 arg_ex2.py -h (or --help)
python3 arg_ex2.py four (for seeing message)
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
	type=int)
args = parser.parse_args()
print(args.square**2)