#!/opt/homebrew/bin/python3

from sys import argv, exit
import re

filepath = argv[1] if len(argv) > 1 else ''
if not filepath or filepath[-6:] != '.gcode':
    print('Usage: replace.py <gcode file> [options]  where options are')
    print(' s:new-speed')
    print(' z:new-Z(down)')
    exit(0)

allStrs = argv[2:] if len(argv) > 2 else []
sStr = ''
zStr = ''
for str in allStrs:
    if str.startswith('s:'):
        sStr = str
    elif str.startswith('z:'):
        zStr = str

speed = sStr[2:] if sStr else ''
z = zStr[2:] if zStr else ''
new_speed = speed if speed.startswith('F') else 'F'+speed if speed else ''
new_z = z if z.startswith('Z') else 'Z'+z if z else ''
old_speed = 'F2000'
old_z = 'Z-1'

if not speed and not z:
    print('Usage: replace.py <gcode file> [options]  where options are')
    print(' s:new-speed')
    print(' z:new-Z(down)')
    exit(1)
    
with open(filepath, 'r') as f:
    content = f.read()
speed_msg = ''
z_msg = ''
pre = ''

if speed:
    content = re.sub(old_speed, new_speed, content)
    speed_msg = f'{old_speed} to {new_speed}'
if z:
    content = re.sub(old_z, new_z, content)
    pre = ', ' if speed else ''
    z_msg = f'{old_z} to {new_z}'

outpath = f'{filepath[:-6]}{new_speed}{new_z}.gcode'
with open(outpath, 'w') as f:
    f.write(content)

print(f'Done, replaced {speed_msg}{pre}{z_msg}')