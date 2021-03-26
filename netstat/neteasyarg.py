#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import argparse
from subprocess import call

"""
Use 2 prog :
netstat
ss
"""

# Options
parser = argparse.ArgumentParser(description = "Quick help to launch netstat with options :")
parser.add_argument("established", help="Display tcp connection established")

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
	print("Nothing to display...")
