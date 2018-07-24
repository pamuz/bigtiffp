# bigtiffp

## Quickstart

```
pip install git+https://github.com/pablo-munoz/bigtiffp
bigtiffp /PATH/TO/SOME/TIFF/FILE
```

## What?

A simple python module that can help you determine if a .tiff file
has bigtiff enabled. It provides a `bigtiff.is_bigtiff(path)` function
that you can use programatically, and a `bigtiffp <file>` command line
application to use from your favorite console.

## Why?

It is not obvious to determine if a .tiff file has bigitiff enabled.
As far as I know `gdalinfo` does not provide such information. In
my work at skycatch we work a lot with .tiff files, so knowing whether
they have bigtiff enabled or not is useful.

## How?

Tiff specification
(https://www.loc.gov/preservation/digital/formats/fdd/fdd000022.shtml)
indicates that a .tiff file should begin with the bytes (magic
numbers) 49 49 2A 00, where the 2A has a decimal representation equal
to 42, which indicates that the file is a normal .tiff file. The
bigtiff specification uses a byte 2B (decimal 43) to indicate that the
file has BIGTIFF enabled. The program opens the given file and
examines the appropriate file to make a decision.
