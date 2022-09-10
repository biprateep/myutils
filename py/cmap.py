import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap


def cmap_white(cmap_name):
    """Returns a colormap with white as the lowest value color."""
    cmap = cm.get_cmap(cmap_name, 256)
    newcolors = cmap(np.linspace(0, 1, 256))
    white = np.array([1, 1, 1, 1])
    newcolors[:1, :] = white
    cmap_white = ListedColormap(newcolors)
    return cmap_white
