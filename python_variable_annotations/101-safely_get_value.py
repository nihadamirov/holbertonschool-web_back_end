#!/usr/bin/env python3
"""module for type-annotated function"""
import typing

T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any, default:
                     typing.Union[T, None] = None) -> \
        typing.Union[typing.Any, T]:
    """Return the value associated with the given key in the dictionary,
    or the default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
