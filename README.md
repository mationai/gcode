# About

Scripts to convert svg files to gcode.

## Running

```sh
optimize.py SVGFILE [optimized-svg-file]
gencode.py SVGFILE [options]
```

The scripts assumes python3 is in brew path. If not, prepend `python3 `.

## Dependencies

* python3, and [vpype-gcode](https://github.com/plottertools/vpype-gcode/):

```sh
pipx install vpype
pipx inject vpype vpype-gcode
```

## Notes

To set the direction of Y in the plotting device, issue the following commands:
```sh
$3=7
$23=7
```

$3=7 inverts Y. $23=7 then inverts Y homing direction so that it continues to home in the correct direction.

Do the same in `cfg.toml` (`invert_y = true`), No `vertical_flip = true`.


## vpype, SVG Notes

Use `linesimplify` before `splitall` [issue 58](https://github.com/abey79/vpype/issues/58).

Layers in SVG via `inkscape:groupmode="layer" inkscape:label="layername"` [Layer names]( https://bylr.info/articles/2023/03/17/layer-names/).


## vpype Notes - Old, maybe outdated

Currently, vpype doesn't know of a bounding box per se (independently of the actual vector content). So for vpype, whenever the bounding box is considered (e.g. for scaleto, to resize correctly), it uses the smallest rectangle that fits whatever vector data is in the pipeline.

Of course, SVG does implement a specific bounding box (with the viewPort, width, height stuff), so this information is actually lost in read. I've considered adding that information into vpype's data model, so that a read/write sequence would maintain the actual margins. [issue 41](https://github.com/abey79/vpype/issues/41)