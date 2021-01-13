import matplotlib.pyplot as plt


def better_step(bin_edges, y, ax=None, **kwargs):
    """A 'better' version of matplotlib's step function

    Given a set of bin edges and bin heights, this plots the thing
    that I wish matplotlib's ``step`` command plotted. All extra
    arguments are passed directly to matplotlib's ``plot`` command.

    Args:
        bin_edges: The bin edges. This should be one element longer than
            the bin heights array ``y``.
        y: The bin heights.
        ax (Optional): The axis where this should be plotted.

    """
    new_x = [a for row in zip(bin_edges[:-1], bin_edges[1:]) for a in row]
    new_y = [a for row in zip(y, y) for a in row]
    if ax is None:
        ax = plt.gca()
    ax.plot(new_x, new_y, **kwargs)
    return ax
