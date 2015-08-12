# Licensed under a 3-clause BSD style license - see LICENSE.rst

from __future__ import print_function, division

import numpy as np

from transform import scalar_type


def randomize(data):
    """
    Randomize data by multiplying existing sigma values by normal deviates.
    """
    # Replicate the sigma values in data.real so they are in data.imag as well.
    data.imag = data.real
    # Generate a view of the real and imaginary parts as a 1D array of
    # real-valued sigmas.
    real_type = scalar_type(data.dtype)
    real_size = 2 * data.size
    sigmas = data.view(real_type).reshape(real_size)
    # Scale each sigma by a normal deviate.  Should break this up into
    # chunks to avoid a large temporary value, but do the simplest thing
    # for now.
    sigmas *= np.random.normal(size=real_size)
    return data