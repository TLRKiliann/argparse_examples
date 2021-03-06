#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import argparse
from subprocess import call

"""
Use :
python3 arg_cmdline.py -ip
python3 arg_cmdline.py -tab
python3 arg_cmdline.py
"""

parser = argparse.ArgumentParser(description = "To launch ifconfig or route -n")
parser.add_argument("-i", "--ip", help="Show me ifconfig")
parser.add_argument("-t", "--tab", help="Show me my route table")

args = parser.parse_args()

ifc = args.ip
rte = args.tab

if args.ip:
    print(call(["ifconfig"]))
elif args.tab:
    print(call(["route"]))
else:
    print("Neither argument is taken into account !!!")
