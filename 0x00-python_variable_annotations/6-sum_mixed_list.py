#!/usr/bin/env python3
"""Typing project."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum the values of a list with different types of elements"""
    return sum(mxd_lst)
