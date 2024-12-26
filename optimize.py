#!/opt/homebrew/bin/python3

import time
from sys import argv, exit
import subprocess

filepathExt = argv[1] if len(argv) > 1 else ''
filepath = filepathExt[:-4] if filepathExt[-4:] == '.svg' else ''

if not filepath:
    print('Usage: optimize.py <svg file> [optimized svg file]')
    exit(0)

outpath = argv[2] if len(argv) > 2 else filepath+'Opt.svg'
args = 'linemerge linesort write'.split(' ')

start_time = time.time()
subprocess.run(['vpype', 'read', filepathExt] + args + [outpath], check=True)
duration = time.time() - start_time
print(f"({duration:.2f} seconds)")
