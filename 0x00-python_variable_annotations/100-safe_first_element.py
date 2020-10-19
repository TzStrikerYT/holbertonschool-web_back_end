#!/usr/bin/env python3
"""Typing project."""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """None return"""
    if lst:
        return lst[0]
    else:
        return None
