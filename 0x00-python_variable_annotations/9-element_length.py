#!/usr/bin/env python3
"""Typing project."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Verify all basics elements of typing"""
    return [(i, len(i)) for i in lst]
