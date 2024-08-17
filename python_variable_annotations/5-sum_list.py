#!/usr/bin/env python3
"""module for type-annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of the floats in the given list."""
    return sum(input_list)
