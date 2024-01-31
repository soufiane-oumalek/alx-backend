#!/usr/bin/python3
""" Basic dictionary """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache Class """
    def put(self, key, item):
        """ assign to the dictionary self.
        cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """
        return the value of key in self.cache_data
        """
        return self.cache_data.get(key, None)
