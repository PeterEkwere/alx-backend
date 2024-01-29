#!/usr/bin/env python3
"""
    Module contains a function that returns a tuple of pagination parameters.
    Author: Peter Ekwere
"""
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple:
    """
    This Function return a tuple of size two
    containing a start index and end index
    corresponding to the range of indexes
    """
    end_index = page_size * page
    start_index = end_index - page_size
    return (start_index, end_index)
