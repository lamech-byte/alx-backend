#!/usr/bin/env python3
"""
Module: 0-simple_helper_function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple containing the start index and end index
    corresponding to the range of indexes to return in a list
    for the given pagination parameters.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index.
    """
    if page < 1 or page_size < 1:
        return (0, 0)

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


if __name__ == "__main__":
    # Test cases
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
