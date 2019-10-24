import matplotlib
from matplotlib import cm as mcm
import numpy as np
from colors.validation import colormaps_valid, n_max


def get_rgb(n=7, colormap='cividis', flip=False):
    if flip:
        colormap += '_r'
    assert colormap in colormaps_valid, f"colormap not accepted: must be one of {repr(colormaps_valid)}"
    assert n in range(0, n_max), f"n not accepted: must be an integer between 0 and {n_max}"
    c = mcm.get_cmap(colormap)
    v = np.arange(0, 1 + 1 / (n - 1), 1 / (n - 1))[0:n]
    # print(v)
    return(list(map(lambda x: matplotlib.colors.rgb2hex(c(x)), v))[0:])
