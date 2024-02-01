#!/usr/bin/env python3
"""4. MRU Caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Class MRUCache.
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """ assign to the dictionary self.
        cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.access_order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = self.access_order.pop()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.access_order.append(key)

    def get(self, key):
        """ return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.
        cache_data, return None.
        """
        if key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
