#!/usr/bin/env python3
"""cache module"""


from typing import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """BasicCache class inherits from BaseCaching"""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Put a key/value pair"""
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # oldest_key = next(iter(self.cache_data))
                oldest_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {oldest_key}")
                # del self.cache_data[oldest_key]

    def get(self, key):
        """Get a key/value pair"""
        if key:
            return self.cache_data.get(key)
        return None
