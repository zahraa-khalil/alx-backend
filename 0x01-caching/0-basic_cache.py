#!/usr/bin/env python3
"""cache module"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class inherits from BaseCaching"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Put a key/value pair"""
        if key and item:
            self.cache_data[key] = item
        return None

    def get(self, key):
        """Get a key/value pair"""
        if key:
            return self.cache_data.get(key)
        return None
