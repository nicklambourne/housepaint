# housepaint

<p align="center">
    <img src="https://github.com/nicklambourne/housepaint/raw/master/docs/img/logo.png" width="250px"/>
</p>

## What is it?
`housepaint` is a demonstration library for a talk on publishing Python packages. A silly little thing with limited 
utility, it allows you to recolor an entire function's worth of text with beautiful, simple decorators.

## Requirements
`housepaint` requires Python >= 3.6.

As of version 0.0.1 it has no dependencies outside the Python standard library, except for `pytest in dev`.

## Installation

Via `poetry`:
```bash
poetry add housepaint
```

Via `pip`:
```bash
pip install housepaint
```

## Usage

```python
from housepaint import BG, FG, paint, Style


@paint(foreground=FG.GREEN, background=BG.BLACK, styles=Style.BOLD)
def success_example() -> None:
    print("This")
    print("Should")
    print("All")
    print("Be")
    print("Green")

success_example()
```

Will result in all of the print output of the function `success_example` being in bold, green font on a black background.

![example of housepaint at work](https://github.com/nicklambourne/housepaint/raw/master/docs/img/example.png)

### Limitations
This library relies on ANSI escape codes to recolour text. If your printed text has ANSI codes there's a good chance it 
won't work out well for you.

## Can I use this in my project?
Yes, please do! The code is all open source and BSD-3-Clause licensed.
