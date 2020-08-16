#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import argparse
from subprocess import call

"""
Use :
python3 arg_netstat.py -e tcp
python3 arg_netstat.py -ep
python3 arg_netstat.py -u udp
python3 arg_netstat.py -uudport
python3 arg_netstat.py -ep -uudport

"""

parser = argparse.ArgumentParser(description = "To launch netstat with options")
parser.add_argument("-e", "--established", help="Display tcp connection established")
parser.add_argument("-p", "--port", help="Display tcp connection established and port")
parser.add_argument("-u", "--udpconn", help="Display udp connection established")
parser.add_argument("--udport", help="Display udp connection established and port")
parser.add_argument("-t", "--tab", help="Show route table")

args = parser.parse_args()

tcp = args.established
udp = args.udpconn
udp_port = args.udport
port = args.port
rte = args.tab

if args.established:
    call(["netstat", "-ante"])

if args.udpconn:
    call(["netstat", "-aune"]) 

if args.udport:
    call(["netstat", "-paune"]) 

if args.port:
    call(["netstat", "-pante"]) 

if args.tab:
    call(["netstat", "-r"])
