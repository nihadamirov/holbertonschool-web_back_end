#!/usr/bin/env python3
"""module for type-annotated function"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of the input list or None if list is empty."""
    if lst:
        return lst[0]
    else:
        return None
