#!/usr/bin/env python3
"""module for type-annotated function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string k and the square of int/float v."""
    return (k, v ** 2)
