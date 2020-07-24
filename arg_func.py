#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import argparse
from subprocess import call

#choice = input("Choice to launch ifconfig or route ? : ")

parser = argparse.ArgumentParser("Description : To launch ifconfig or route -n")
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
    print("Neither is taken into account !!!")
