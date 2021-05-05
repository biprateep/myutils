import numpy as np
import matplotlib.pyplot as plt


def better_step(bin_edges, y, yerr=None, ax=None, **kwargs):
    """A 'better' version of matplotlib's step function

    Given a set of bin edges and bin heights, this plots the thing
    that I wish matplotlib's ``step`` command plotted. All extra
    arguments are passed directly to matplotlib's ``plot`` command.

    Args:
        bin_edges: The bin edges. This should be one element longer than
            the bin heights array ``y``.
        y: The bin heights.
        yerr: symmetric error on y.
        ax (Optional): The axis where this should be plotted.

    """
    new_x = [a for row in zip(bin_edges[:-1], bin_edges[1:]) for a in row]
    new_y = [a for row in zip(y, y) for a in row]
    if ax is None:
        ax = plt.gca()
    p = ax.plot(new_x, new_y, **kwargs)
    if yerr is not None:
        new_yerr = np.array([a for row in zip(yerr, yerr) for a in row])
        ax.fill_between(
            new_x, new_y + new_yerr, new_y - new_yerr, alpha=0.1, color=p[0].get_color()
        )
    return ax


def hist_on_binned_array(hist, edges, ax=None, **kwargs):
    """Plot histogram with already binned data

    Parameters
    ----------
    hist : ndarray of size n
        population in each bin
    edges : ndarray of size n+1
        bin edges
    ax : matplotlib axis object, optional
        existing matplotlib axis to plot on, by default None

    Returns
    -------
    n, edges, pathces: the default output from plt.hist
    """
    if ax is None:
        ax = plt.gca()
    x = (edges[1:] + edges[:-1]) / 2
    n, edges, patches = ax.hist(x, weights=hist, bins=edges, **kwargs)
    return n, edges, patches


def hist2d_on_binned_array(hist, xedges, yedges, colorbar=False, ax=None, **kwargs):
    """Plot histogram with already 2D binned data

    Parameters
    ----------
    hist : ndarray of size m,n
        population in each bin
    xedges : ndarray of size n+1
        bin edges along x axis
    yedges : ndarray of size m+1
        bin edges along y axis
    colorbar : bool, optional
        whether to add colorbar, by default False
    ax : matplotlib axis object, optional
        existing matplotlib axis to plot on, by default None

    Returns
    -------
    h, xedges, yedges, im
        the default output from plt.hist2d
    """
    if ax is None:
        ax = plt.gca()
    xdata = (xedges[1:] + xedges[:-1]) / 2
    ydata = (yedges[1:] + yedges[:-1]) / 2
    xv, yv = np.meshgrid(xdata, ydata)
    x = xv.ravel()
    y = yv.ravel()
    z = hist.T.ravel()
    h, xedges, yedges, im = ax.hist2d(x, y, weights=z, bins=(xedges, yedges), **kwargs)
    if colorbar:
        cb = ax.figure.colorbar(im, ax=ax)
    return h, xedges, yedges, im