#!/usr/bin/env python3
"""
0x00. Pagination
"""
from typing import Dict
simple_pagination = __import__('1-simple_pagination').Server


class Server:
    """Server Class"""
    def __init__(self):
        """Initialization method"""
        self.server = simple_pagination()

    def get_hyper(self, page: int, page_size: int) -> Dict:
        """
        returns a dictionary containing key-value pairs
        """

        data = self.server.get_page(page, page_size)
        total_items = len(self.server.dataset())
        total_pages = (total_items + page_size - 1)

        metadata = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

        return metadata
