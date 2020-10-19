#!/usr/bin/env python3
"""Typing project."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Pass an union in typing"""
    return k, v ** 2
