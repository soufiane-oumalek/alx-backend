#!/usr/bin/env python3
"""2. LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Class LIFOCache.
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ assign to the dictionary self.
        cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            disc_key = self.stack.pop()
            del self.cache_data[disc_key]
            print(f"DISCARD: {disc_key}")

        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item if found, None otherwise.
        """
        return self.cache_data.get(key)
