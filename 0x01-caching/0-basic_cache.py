#!/usr/bin/python3
"""
0x01. Caching
"""
from base_caching import BaseCaching



class BasicCache(BaseCaching):
    """caching class"""
    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        self.cache_data.get(key, None)
