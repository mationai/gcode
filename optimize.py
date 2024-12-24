#!/opt/homebrew/bin/python3

import time
from sys import argv, exit
import subprocess

filepath = argv[1] if len(argv) > 1 and argv[0].startswith('optimize') else argv[0]
filename = filepath[:-4] if filepath[-4:] == '.svg' else ''

if not filename:
    print('Usage: optimize.py <svg file> [optimized svg file]')
    exit(0)

outpath = argv[2] if len(argv) > 2 and argv[0].startswith('optimize') else filename+'Opt.svg'

args = 'linemerge linesort reloop write'.split(' ')

start_time = time.time()
subprocess.run(['vpype', 'read', filepath] + args + [outpath], check=True)
duration = time.time() - start_time
print(f"({duration:.2f} seconds)")