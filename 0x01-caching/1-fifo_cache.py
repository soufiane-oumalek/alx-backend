#!/usr/bin/env python3
"""1. FIFO caching.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represents a caching system that uses First-In First-Out (FIFO) eviction policy.
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adds an item in the cache.

        Args:
            key: The key of the item.
            item: The item to be stored.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = self.queue.pop(0)
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item if found, None otherwise.
        """
        return self.cache_data.get(key)
