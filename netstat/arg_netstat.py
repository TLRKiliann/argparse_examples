#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import argparse
from subprocess import call

"""
Use :
python3 arg_netstat.py -e tcp
python3 arg_netstat.py -established
python3 arg_netstat.py -port
python3 arg_netstat.py -u udp
python3 arg_netstat.py -udport
python3 arg_netstat.py -table
python3 arg_netstat.py -t route

"""

# Options
parser = argparse.ArgumentParser(description = "Quick help to launch netstat with options :")
parser.add_argument("-e", "--established", help="Display tcp connection established")
parser.add_argument("-p", "--port", help="Display tcp connection established and port")
parser.add_argument("-u", "--udpconn", help="Display udp connection established")
parser.add_argument("--udport", help="Display udp connection established and port")
parser.add_argument("-t", "--table", help="Show route table")

args = parser.parse_args()

# args
tcp = args.established
port = args.port
udp = args.udpconn
udp_port = args.udport
route = args.table

if args.established:
    call(["netstat", "-ante"])

if args.udpconn:
    call(["netstat", "-aune"]) 

if args.udport:
    call(["netstat", "-paune"]) 

if args.port:
    call(["netstat", "-pante"]) 

if args.table:
    call(["netstat", "-r"])
