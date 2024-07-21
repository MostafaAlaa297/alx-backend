#!/usr/bin/env python3
"""
0x00. Pagination
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
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
            takes two integer arguments page with default value 1
            and page_size with default value 10
            """

            assert isinstance(page, int), "page must be an integer"
            assert page > 0, "page must be greater than 0"
            assert isinstance(page_size, int), "page_size must be an integer"
            assert page_size > 0, "page_size must be greater than 0"

            self.dataset()

            start, end = index_range(page, page_size)

            if start >= len(self.__dataset):
                return []

            return self.__dataset[start:end]
