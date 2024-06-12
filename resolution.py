"""Module working on resolution."""


def return_resolution(n):
    """Function returning resolution.

    Usage examples:
    >>> return_resolution(1.9009)
    4
    >>> return_resolution(1)
    0
    >>> return_resolution(0.000000000001)
    12
    >>> return_resolution(0.0000000000002)
    Traceback (most recent call last):
    OverflowError: int too large to convert to float
    """

    resolution = 0
    while ((n * 10**resolution) // 1) != (n * 10**resolution) or resolution > 12:
        resolution = resolution + 1
    return resolution
