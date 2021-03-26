#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import argparse
from subprocess import call

"""
Use :
python3 arg_netstat.py -tsoc tcp
python3 arg_netstat.py --tsocket tcp

python3 arg_netstat.py -usoc udp
python3 arg_netstat.py --usocket udp

python3 arg_netstat.py -t r
python3 arg_netstat.py --tab r
"""

# Options
parser = argparse.ArgumentParser(description = "Quick help to "\
	"launch netstat with options :")
parser.add_argument("-tsoc", "--tsocket", dest='tsox',
	help="Display tcp connection established")
parser.add_argument("-usoc", "--usocket", dest='usox',
	help="Display tcp connection established and port")
parser.add_argument("-t", "--tab", dest="table",
	help="Show route table")

args = parser.parse_args()

# args
tcpsoc = args.tsox
udpsoc = args.usox
route = args.table

if args.tsox=='tcp':
    call(["netstat", "-pante"])

if args.usox=='udp':
    call(["netstat", "-paune"]) 

if args.table=='r':
    call(["netstat", "-r"])
