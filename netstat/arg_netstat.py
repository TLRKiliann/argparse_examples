#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import argparse
from subprocess import call

"""
For example with too many args
Use :
python3 arg_netstat.py -tsoc tcp
python3 arg_netstat.py --tsocket tcp

python3 arg_netstat.py -usoc udp
python3 arg_netstat.py --usocket udp

python3 arg_netstat.py -atcp conntcp
python3 arg_netstat.py --all_tcp conntcp

python3 arg_netstat.py -audp connudp
python3 arg_netstat.py --all_udp connudp

python3 arg_netstat.py -t r
python3 arg_netstat.py --tab r
"""

# Options
parser = argparse.ArgumentParser(description = "Quick help to "\
    "launch netstat with options :")
parser.add_argument("-tsoc", "--tsocket", dest='tsox',
    help="Display tcp connection established and socket port")
parser.add_argument("-usoc", "--usocket", dest='usox',
    help="Display tcp connection established and socket port")
parser.add_argument("-atcp", "--all_tcp", dest='alltcp',
    help="Display all tcp connections")
parser.add_argument("-audp", "--all_udp", dest='alludp',
    help="Display all udp connections")
parser.add_argument("-t", "--tab", dest="table",
    help="Show route table")

args = parser.parse_args()

# args
tcpsoc = args.tsox
udpsoc = args.usox
tcpall = args.alltcp
udpall = args.alludp
route = args.table

if args.tsox=='tcp':
    call(["netstat", "-pante"])

if args.usox=='udp':
    call(["netstat", "-paune"]) 

if args.alltcp == 'conntcp':
    call(["netstat", "-ante"])

if args.alludp == 'connudp':
    call(["netstat", "-anue"])

if args.table=='r':
    call(["netstat", "-r"])
