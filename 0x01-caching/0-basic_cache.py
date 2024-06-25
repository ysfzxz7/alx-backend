#!/usr/bin/env python3
"""
    Module of class 'BasicCache' that inherits
    from 'BaseCaching' and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
        BasicCache class the inherits from BaseCaching
    """
    def __init__(self):
        """
            Constructure of BasicCache
        """
        super().__init__()

    def put(self, key, item):
        """
            Method that puts new items to cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
            Method that returns the value of the given key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
