ds9norm
=======

This file implements a matplotlib Normalize object
which mimics the functionality of image scaling functions in [ds9](http://ds9.si.edu/site/Home.html). It provides several ways of configuring image scaling:

  - Clipping the low and high intensities at specified percentiles (`clip_lo`, `clip_hi`)
  - Specifying an intensity transfer function for ramping from black to white
    (`stretch`)
  - Setting the mid-point of this transfer function (`bias`, akin to dragging
    the right mouse button left/right in ds9)
  - Setting how sharp the transition from black-white is (`contrast`, akin
    to dragging the right mouse button up/down in ds9)

Examples
--------

See the [example notebook](http://nbviewer.ipython.org/github/glue-viz/ds9norm/blob/master/Examples.ipynb)

```python

data = fits.getdata('M51.fits')
figure, axs = plt.subplots(ncols=4, nrows=4, squeeze=False, tight_layout=True)

for ax, stretch in zip(axs[0], ['linear', 'sqrt', 'arcsinh', 'log']):
    ax.imshow(data, norm=DS9Normalize(stretch=stretch))
    ax.set_title(stretch)

for ax, contrast in zip(axs[1], [0.5, 1, 2, -1]):
    ax.imshow(data, norm=DS9Normalize(contrast=contrast))
    ax.set_title('Contrast = %0.1f' % contrast)

for ax, bias in zip(axs[2], [.2, .5, .8, .9]):
    ax.imshow(data, norm=DS9Normalize(bias=bias))
    ax.set_title('Bias = %0.1f' % bias)

for ax, (lo, hi) in zip(axs[3], [(0, 100), (1, 99), (5, 95), (10, 90)]):
    im = ax.imshow(data, norm=DS9Normalize(clip_lo=lo, clip_hi=hi))
    ax.set_title('%i-%i%%' % (lo, hi))
```

![ds9norm demo](gallery.png)

Build Status
------------

[![Build Status](https://travis-ci.org/glue-viz/ds9norm.png)]
(https://travis-ci.org/glue-viz/ds9norm?branch=master)
[![Coverage Status](https://coveralls.io/repos/glue-viz/ds9norm/badge.png)]
(https://coveralls.io/r/glue-viz/ds9norm)