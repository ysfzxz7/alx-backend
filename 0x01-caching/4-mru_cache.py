#!/usr/bin/env python3
"""
    Module of class MRUCache that inherits from BaseCaching and is a
    caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
        MRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
            MRUCache constructure
        """
        self.blocks = []
        super().__init__()

    def put(self, key, item):
        """
            Method that puts key and its item in cache
            with MRU algorithm
        """
        if key and item:
            if len(self.cache_data) < self.MAX_ITEMS:
                if key in self.cache_data:
                    self.blocks.remove(key)
                self.blocks.append(key)
                self.cache_data[key] = item
            else:
                if key in self.cache_data:
                    self.blocks.remove(key)
                    self.blocks.append(key)
                    self.cache_data[key] = item
                else:
                    k = self.blocks.pop()
                    self.blocks.append(key)
                    self.cache_data[key] = self.cache_data.pop(k)
                    self.cache_data[key] = item
                    print(f'DISCARD: {k}')

    def get(self, key):
        """
            Method that returns the value if the given key
        """
        if key and key in self.cache_data:
            self.blocks.remove(key)
            self.blocks.append(key)
            return self.cache_data[key]
        return None
