#!/usr/bin/python3
# -*- encoding:utf-8 -*-


"""
Use : 
python3 arg_ex1.py echo
Verbose message :
python3 arg_ex1.py --help
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print(args.echo)