#!/usr/bin/env python3
"""module for type-annotated function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing each element of the input list
    along with its length.
    """
    return [(i, len(i)) for i in lst]
