#!/usr/bin/env python3
"""find the correct indexes to paginate the dataset"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """return a tuple of size two"""
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def _init_(self):
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
        """Get a page of data from the dataset."""
        assert isinstance(page, int) and isinstance(page_size, int), \
            "AssertionError raised when page and/or page_size are not ints"
        assert page > 0 and page_size > 0, "AssertionError raised with 0"
        assert page > 0 and page_size > 0, \
            "AssertionError raised with negative values"

        start, end = index_range(page, page_size)

        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]
