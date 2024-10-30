#!/usr/bin/env python3
"""cache module"""


from typing import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """BasicCache class inherits from BaseCaching"""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Put a key/value pair"""

        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            second_to_last_key = keys[-2]
            print(f"DISCARD: {second_to_last_key}")
            del self.cache_data[second_to_last_key]

    def get(self, key):
        """Get a key/value pair"""
        if key:
            return self.cache_data.get(key)
        return None
