# About

Scripts to convert svg files to gcode.

# Running

```sh
optimize.py SVGFILE [optimized-svg-file]
gencode.py SVGFILE [gcode-file]
```

The scripts assumes python3 is in brew path. If not, prepend `python3 `.

# Dependencies

* python3, and [vpype-gcode](https://github.com/plottertools/vpype-gcode/):

```sh
pipx install vpype
pipx inject vpype vpype-gcode
```

# Notes

To set the direction of Y in the plotting device, issue the following commands:
```sh
$3=7
$23=7
```

$3=7 inverts Y. $23=7 then inverts Y homing direction so that it continues to home in the correct direction.

Do the same in `cfg.toml` (`invert_y = true`), No `vertical_flip = true`.