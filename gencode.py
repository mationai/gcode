#!/opt/homebrew/bin/python3

from math import e
import time
from sys import argv, exit
import subprocess

filepath = argv[1] if len(argv) > 1 and argv[0].startswith('gencode') else argv[0]
filename = filepath[:-4] if filepath[-4:] == '.svg' else ''

if not filename:
    print('Usage: gencode.py <svg file> [options]  where options are')
    print(' layout options if prefixed with l. All units in mm. Eg.:')
    print(' l:m30,a4 or l:m20,220x240')
    print(' st220x300 (scale to x, y, no "," if only option)')
    exit(0)

svgname = filename[:-3] if filename[-3:] == 'Opt' else filename
allStrs = argv[2:] if len(argv) > 2 and argv[0].startswith('gencode') else []
loStr = ''
if allStrs:
    if allStrs[0].startswith('l:'):
        loStr = allStrs.pop(0)
    if len(allStrs) > 1 and allStrs[1].startswith('l:'):
        loStr = allStrs.pop(1)
opStr = allStrs[0] if allStrs else ''
opStrs = opStr.split(',') if opStr else []
loStrs = loStr[2:].split(',') if loStr else []
# print('allStrs', allStrs, 'loStr', loStr, 'opStr', opStr, 'opStrs', opStrs)

options = []
lOptions = []
for s in opStrs:
    if s[0:2] == 'st':
        x, y = s[2:].split('x')
        options.extend(['scaleto', x+'mm', y+'mm'])
        svgname += '_st' + x + 'x' + y
    else:
        raise Exception("Option "+s+" not implemented yet.")

for i, s in enumerate(loStrs):
    if s in "tight a6 a5 a4 a3 a2 a1 a0 letter legal executive tabloid".split(' '):
        if i < len(loStrs) - 1:
            raise Exception("Page size needs to be last layout option")
        lOptions.extend([s])
        svgname += '_' + s
    elif s[0] == 'm':
        lOptions.extend(['-m', s[1:]+'mm'])
        svgname += '_m' + s[1:]
    elif 'x' in s and not s.startswith('x'):
        lOptions.extend([s+'mm'])
        svgname += '_' + s
    else:
        raise Exception("Layout option "+s+" not implemented yet.")

args = 'vpype -c cfg.toml'.split(' ') 
rargs = ['read', filepath]
wargs = 'gwrite -p plotter'.split(' ')
layOpts = ['layout'] + lOptions
outpath = svgname+'.gcode'

start_time = time.time()
print('cmd: ', ' '.join(args + rargs + options + layOpts + wargs + [outpath]))
subprocess.run(args + rargs + options + layOpts + wargs + [outpath], check=True)
duration = time.time() - start_time
print(f"({duration:.2f} seconds)")
