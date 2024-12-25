#!/usr/bin/env python3

from hmac import new
from sys import argv, exit
import re

def replace_speed(filepath, new_speed, old_speed):
    """Replace feed rate speed in G-code file"""
    with open(filepath, 'r') as f:
        content = f.read()
    new_content = re.sub(old_speed, new_speed, content)

    with open(filepath, 'w') as f:
        f.write(new_content)

def main():
    filepath = argv[1] if len(argv) > 1 else ''
    new_speed = argv[2] if len(argv) > 2 else ''
    old_speed = argv[3] if len(argv) > 3 else 'F2000'
    if not new_speed:
        print('Usage: setspeed.py <gcode file> <new speed> [old speed]')
        exit(1)
        
    replace_speed(filepath,
     new_speed if new_speed.startswith('F') else 'F'+new_speed,
     old_speed if old_speed.startswith('F') else 'F'+old_speed)
    print(f'Done, replaced', old_speed, 'with', new_speed)

if __name__ == '__main__':
    main()
