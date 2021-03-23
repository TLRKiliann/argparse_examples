#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import argparse
from subprocess import call

"""
Use :
python3 arg_netstat2.py --help
python3 arg_netstat2.py -e tcp
python3 arg_netstat2.py -e netstat
python3 arg_netstat2.py -ep
python3 arg_netstat2.py -e tcport
python3 arg_netstat2.py -u udp
python3 arg_netstat2.py -u netstat
python3 arg_netstat2.py -u udport
python3 arg_netstat2.py -u netstat
python3 arg_netstat2.py -ep -udport
python3 arg_netstat2.py -t tab
python3 arg_netstat2.py -t netstat
python3 arg_netstat2.py -t rte
"""


def main():
    tcp = args.established
    udp = args.udpconn
    udp_port = args.udport
    tport = args.tcport
    rte = args.tab


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--established", help="Display tcp connection established")
    parser.add_argument("--tcport", help="Display tcp connection established and port")
    parser.add_argument("-u", "--udpconn", help="Display udp connection established")
    parser.add_argument("--udport", help="Display udp connection established and port")
    parser.add_argument("-t", "--tab", help="Show route table")
    args = parser.parse_args()

    if args.established:
        call(["netstat", "-ante"])

    if args.udpconn:
        call(["netstat", "-aune"])

    if args.udport:
        call(["netstat", "-paune"]) 

    if args.tcport:
        call(["netstat", "-pante"]) 

    if args.tab:
        call(["netstat", "-r"])
