#!/usr/bin/python3
# -*- encoding:utf-8 -*-


import argparse
import datetime
import time

"""
python3 arg_time.py --now std
python3 arg_time.py --now iso
python3 arg_time.py --now unix
python3 arg_time.py --now tz
"""

parser = argparse.ArgumentParser()

parser.add_argument('--now', dest='format', choices=['std', 'iso', 'unix', 'tz'],
                    help="shows datetime in given format")

args = parser.parse_args()
fmt = args.format

if fmt == 'std':
    print(datetime.date.today())
elif fmt == 'iso':
    print(datetime.datetime.now().isoformat())
elif fmt == 'unix':
    print(time.time())
elif fmt == 'tz':
    print(datetime.datetime.now(datetime.timezone.utc))
