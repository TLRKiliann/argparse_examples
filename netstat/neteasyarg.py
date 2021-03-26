#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import argparse
from subprocess import call

"""
Use cmd :
python3 neteasyarg.py -nt
python3 neteasyarg.py -nu
...
"""

# Options
parser = argparse.ArgumentParser(description = "Quick help to launch netstat with options :")
parser.add_argument("established", help="Display tcp/udp connections established")

args = parser.parse_args()

if args.established == 'nt':
    call(["netstat", "-ante"])
elif args.established == 'nu':
    call(["netstat", "-anue"])
elif args.established == 'sst':
    call(["ss", "-nlt"])
elif args.established == 'ssu':
    call(["ss", "-nlu"])
elif args.established == 'nr':
    call(["netstat", "-r"])
else:
    print("Use one of following options : nt - nu - sst - ssu -r")
