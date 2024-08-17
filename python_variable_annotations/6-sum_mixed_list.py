#!/usr/bin/env python3
"""module for type-annotated function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of integers and floats in the given mixed list."""
    return sum(mxd_lst)
