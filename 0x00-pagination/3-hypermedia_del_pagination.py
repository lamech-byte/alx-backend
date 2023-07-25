#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict
from typing import List


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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary containing the hypermedia information for the
        requested index.

        Args:
            index (int, optional): The start index of the return page.
            Defaults to None.
            page_size (int, optional): Number of items per page. Defaults to 10.

        Returns:
            Dict: A dictionary containing hypermedia information.
        """
        assert index is None or isinstance(index, int) and index >= 0, """
        Index must be a non-negative integer."""
        assert isinstance(page_size, int) and page_size > 0, """Page
        size must be a positive integer."""

        total_items = len(self.indexed_dataset())
        if index is None or index >= total_items:
            return {}

        data = []
        for i in range(index, total_items):
            if len(data) == page_size:
                break
            if i in self.indexed_dataset():
                data.append(self.indexed_dataset()[i])

        next_index = None
        for i in range(index + 1, total_items):
            if i in self.indexed_dataset():
                next_index = i
                break

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index,
        }


if __name__ == "__main__":
    # Test cases
    server = Server()

    server.indexed_dataset()

    try:
        server.get_hyper_index(300000, 100)
    except AssertionError:
        print("AssertionError raised when out of range")

    index = 3
    page_size = 2

    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 1- request first index
    res = server.get_hyper_index(index, page_size)
    print(res)

    # 2- request next index
    print(server.get_hyper_index(res.get('next_index'), page_size))

    # 3- remove the first index
    del server._Server__indexed_dataset[res.get('index')]
    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 4- request again the initial index -> the first data retrieved
    print(server.get_hyper_index(index, page_size))

    # 5- request again the initial next index -> same data page as the request
    print(server.get_hyper_index(res.get('next_index'), page_size))
