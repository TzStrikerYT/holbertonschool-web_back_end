#!/usr/bin/env python3
""" pagination project"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return the start of index and the end of index corresponding
        to th rainge of indexes """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
