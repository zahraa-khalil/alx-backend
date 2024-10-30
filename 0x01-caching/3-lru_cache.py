from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class that discards the least recently used items first"""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add item to the cache and discard LRU item if limit is exceeded"""
        if key and item:
            # If the key already exists, remove it to update its position
            if key in self.cache_data:
                self.cache_data.pop(key)

            # Add the item as the most recently used
            self.cache_data[key] = item

            # Check if we exceed MAX_ITEMS
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Pop the first item (least recently used)
                oldest_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Retrieve item from cache and mark it as recently used"""
        if key in self.cache_data:
            # Move the accessed item to the end to mark it as recently used
            item = self.cache_data.pop(key)
            self.cache_data[key] = item
            return item
        return None
