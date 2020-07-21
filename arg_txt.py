#!/usr/bin/python3
# -*- encoding:utf-8 -*-

"""
python3 arg_txt.py words.txt 6
"""


import argparse
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument('f', type=str, help="file name")
parser.add_argument('n', type=int, help="show n lines from the top")

args = parser.parse_args()

filename = args.f # f

lines = Path(filename).read_text().splitlines()

for line in lines[:args.n]: # n
	print(line)