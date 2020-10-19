#!/usr/bin/env python3
"""Typing project."""
from typing import Union, Mapping, Any, TypeVar

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """Put my own type"""
    if key in dct:
        return dct[key]
    else:
        return default
