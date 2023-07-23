#!/usr/bin/env python3
"""
Module: 2-hypermedia_pagination
"""

import csv
import math
from typing import List
from typing import Dict
from typing import Union


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of
        the dataset (i.e. the correct list of rows)
        based on the given pagination parameters.

        Args:
            page (int, optional): Page number (1-indexed). Defaults to 1.
            page_size (int, optional): Number of
            items per page. Defaults to 10.

        Returns:
            List[List]: The list of rows corresponding to the requested page.
        """
        assert isinstance(page, int) and page > 0, """Page must be a
        positive integer."""
        assert isinstance(page_size, int) and page_size > 0, """Page
        size must be a positive integer."""

        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index]

    def get_hyper(
        self, page: int = 1,
        page_size: int = 10) -> Dict[str, Union[int, List[List], None]]:
        """
        Return a dictionary containing the
        hypermedia information for the requested page.

        Args:
            page (int, optional): Page number (1-indexed). Defaults to 1.
            page_size (int, optional): Number of items per
            page. Defaults to 10.

        Returns:
            Dict: A dictionary containing hypermedia information.
        """
        assert isinstance(page, int) and page > 0, """Page must be a
        positive integer."""
        assert isinstance(page_size, int) and page_size > 0, """Page
        size must be a positive integer."""

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }


if __name__ == "__main__":
    # Test cases
    server = Server()

    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))
