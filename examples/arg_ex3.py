#!/usr/bin/python3
# -*- encoding:utf-8 -*-


"""
Use :
python3 arg_ex3.py --verbosity 1 (or anything else)
python3 arg_ex3.py --verbosity (error)
python3 arg_ex3.py --help
python3 arg_ex3.py (no error)
"""


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on !")