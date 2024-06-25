#!/usr/bin/env python3
"""
    Module of class LIFOCache that inherits from BaseCaching and is a
    caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
        LIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
            LIFOCache class constructure
        """
        super().__init__()

    def put(self, key, item):
        """
            Method that puts key and its item in cache
            using LIFO algorithm
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.LIFO_KEY = key
                return
            if len(self.cache_data) == self.MAX_ITEMS:
                k = None
                if self.LIFO_KEY:
                    k = self.LIFO_KEY
                else:
                    k = list(self.cache_data.keys())[-1]
                del self.cache_data[k]
                print(f'DISCARD: {k}')
            self.LIFO_KEY = key
            self.cache_data[key] = item

    def get(self, key):
        """
            Method that returns value of the given key
            from cache
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
