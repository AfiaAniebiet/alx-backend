#!/usr/bin/env python3

"""Function index_range that takes two arguments
and returns a tuple of size two containing a start
and an end index corresponding to the range of indexes
to return in alist for those particular pagination
parameters"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns Tuple containing pagination start index and end index"""
    return ((page_size * (page - 1)), page_size * page)
