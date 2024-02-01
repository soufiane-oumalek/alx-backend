#!/usr/bin/env python3
"""LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Class LRUCach
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ assign to the dictionary self.
        cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = self.queue.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """ return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.
        cache_data, return None.
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
