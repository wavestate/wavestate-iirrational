"""
Contains setup functions for test data, these are returned in a QuickBunch dictionary, with some annotation about the number of data sets
"""

from . import simple_set_1
from . import random_sets

from ..data2testcase import (
    data2testcase,
    testcase2data,
)

from .utilities import (
    assert_almost_equal,
)

datasets = {}
datasets.update(simple_set_1.datasets)
datasets.update(random_sets.datasets)


def IIRrational_data(
    name,
    set_num = 0,
    instance_num = 0,
    **kwargs
):
    return datasets[name].generator(
        sN = set_num,
        iN = instance_num,
        **kwargs
    )


__all__ = [
    assert_almost_equal,
    data2testcase,
    testcase2data,
    IIRrational_data,
    datasets,
]
