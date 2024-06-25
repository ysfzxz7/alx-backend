#!/usr/bin/env python3
"""
    Module of class LRUCache that inherits from BaseCaching and is a
    caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
        LRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
            LRUCache constructure
        """
        self.blocks = []
        super().__init__()

    def put(self, key, item):
        """
            Method that puts new key and its value in cache
            with the LRU algorithm
        """
        if key and item:
            if len(self.cache_data) < self.MAX_ITEMS:
                if key in self.cache_data:
                    self.blocks.remove(key)
                    self.blocks.append(key)
                    self.cache_data[key] = item
                else:
                    self.blocks.append(key)
                    self.cache_data[key] = item
            else:
                if key in self.cache_data:
                    self.blocks.remove(key)
                    self.blocks.append(key)
                    self.cache_data[key] = item
                else:
                    k = self.blocks[0]
                    self.cache_data[key] = self.cache_data.pop(k)
                    self.cache_data[key] = item
                    del self.blocks[0]
                    self.blocks.append(key)
                    print(f'DISCARD: {k}')

    def get(self, key):
        """
            Method that returns the value of the given key
        """
        if key and key in self.cache_data:
            self.blocks.remove(key)
            self.blocks.append(key)
            return self.cache_data[key]
        return None
