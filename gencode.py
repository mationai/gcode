#!/opt/homebrew/bin/python3

import time
from sys import argv, exit
import subprocess

filepath = argv[1] if len(argv) > 1 and argv[0].startswith('gencode') else argv[0]
filename = filepath[:-4] if filepath[-4:] == '.svg' else ''

if not filename:
    print('Usage: gencode.py <svg file> [gcode file]')
    exit(0)

outpath = argv[2] if len(argv) > 2 and argv[0].startswith('gencode') else filename+'.gcode'

args = 'vpype --config cfg.toml read'.split(' ') 
wargs = 'gwrite -p plotter'.split(' ')

start_time = time.time()
subprocess.run(args + [filepath] + wargs + [outpath], check=True)
duration = time.time() - start_time
print(f"({duration:.2f} seconds)")
