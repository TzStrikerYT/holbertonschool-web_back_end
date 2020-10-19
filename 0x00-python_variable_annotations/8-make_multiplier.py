#!/usr/bin/env python3
"""Typing project."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function callable"""
    def a(n: float) -> float:
        """Return the multiplication of two numbers"""
        return n * multiplier
    return a
