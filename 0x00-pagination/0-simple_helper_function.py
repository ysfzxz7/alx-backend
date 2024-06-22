#!/usr/bin/env python3
"""
    Module of simple helper
"""


def index_range(page: int, page_size: int) -> tuple:
    """
        Function that returns a tupe contains
        data that should be returned
    """
    res = ((page - 1) * page_size, page * page_size)
    return res
