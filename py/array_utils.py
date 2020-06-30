import numpy as np
from scipy import stats

def to_percentile(a, kind="rank"):
    """
    converts array elements to their percentile value.
    This behaves like scipy.stats.percentileofscore but acts on the whole array
    """
    assert a.ndim == 1, "Only 1D arrays are supported"
    
    kinds = {"rank":"average", "weak":"max", "strict":"min", "mean":"mean"}
    assert kind in kinds.keys(), "Supported value for kind"
    
    if kind in ["rank", "average"]:
        return stats.rankdata(a, kinds[kind])*100/len(a)
    if kind == "strict":
        return (stats.rankdata(a, 'min')-1)*100/len(a)
    if kind == "mean":
        return (stats.rankdata(a, 'max') + (stats.rankdata(a, 'min')-1))*100/(2*len(a))
