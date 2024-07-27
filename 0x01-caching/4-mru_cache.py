#!/usr/bin/python3
"""
0x01. Caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """caching class"""
    def __init__(self):
        """Initialization function"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) >= self.MAX_ITEMS:
            last_key = next(reversed(self.cache_data))
            print(f"DISCARD: {last_key}")
            self.cache_data.pop(last_key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
