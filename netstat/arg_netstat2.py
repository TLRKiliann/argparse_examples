#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import argparse
from subprocess import call

"""
Use :
python3 arg_netstat2.py --help
python3 arg_netstat2.py -t etcp

python3 arg_netstat2.py -udpconn
python3 arg_netstat2.py -u udp

python3 arg_netstat2.py -info
python3 arg_netstat2.py -i info

python3 arg_netstat2.py -r tab
python3 arg_netstat2.py -r netstat
"""


def main():
    tcp = args.etcp
    tport = args.alltcp
    udp = args.udpconn
    man = args.info
    rte = args.tab


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--etcp", help="Display tcp connection established")
    parser.add_argument("-t", "--alltcp", help="Display tcp connection established and port")
    parser.add_argument("-u", "--udpconn", help="Display udp connection established")
    parser.add_argument("-i", "--info", help="Display man netstat - help")
    parser.add_argument("-r", "--tab", help="Show route table")
    args = parser.parse_args()

    if args.etcp:
        call(["netstat", "-ante"])

    if args.alltcp:
        call(["netstat", "-te"])

    if args.udpconn:
        call(["netstat", "-aune"])

    if args.info:
        call(["man", "netstat"])

    if args.tab:
        call(["netstat", "-r"])
