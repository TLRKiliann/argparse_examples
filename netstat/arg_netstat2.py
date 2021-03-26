#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import argparse
from subprocess import call

"""
Use :
python3 arg_netstat.py -a all

python3 arg_netstat.py -conn tcp
python3 arg_netstat.py --connection tcp

python3 arg_netstat.py -conn udp
python3 arg_netstat.py --connection udp

python3 arg_netstat.py -conn atcp
python3 arg_netstat.py --connection atcp

python3 arg_netstat.py -conn audp
python3 arg_netstat.py --connnection audp

python3 arg_netstat.py -t r
python3 arg_netstat.py --tab r
"""

# Options
parser = argparse.ArgumentParser(description = "Quick help to "\
    "launch netstat with options :")
parser.add_argument("-a", "--all", dest = 'net', help = "To launch netstat")
parser.add_argument("-conn", "--connection", dest = 'tsox',
    help = "To use options with connection and socket port")
parser.add_argument("-t", "--tab", dest = "table", help = "Show route table")

args = parser.parse_args()

# args
netlaunch = args.net
tcpsoc = args.tsox
route = args.table

if args.net == 'all':
    call(["netstat"])

if args.tsox == 'tcp':
    call(["netstat", "-pante"])

if args.tsox == 'udp':
    call(["netstat", "-paune"]) 

if args.tsox == 'atcp':
    call(["netstat", "-ante"])

if args.tsox == 'audp':
    call(["netstat", "-anue"])

if args.table == 'r':
    call(["netstat", "-r"])
