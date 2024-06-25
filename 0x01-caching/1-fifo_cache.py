#!/usr/bin/env python3
"""
    Module of class 'FIFOCache' that inherits from 'BaseCaching' and is a
    caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
        FIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
            Constructor of FIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """
            Method that puts data in cache with FIFO method
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) == self.MAX_ITEMS:
                k = list(self.cache_data.keys())[0]
                del self.cache_data[k]
                print(f'DISCARD: {k}')
            self.cache_data[key] = item

    def get(self, key):
        """
            Method that returns the value of the given key
            from cache_data
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
