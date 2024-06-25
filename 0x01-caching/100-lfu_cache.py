#!/usr/bin/env python3
"""
    Module of class 'LFUCache' that inherits from 'BaseCaching' and is a
    caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
        LFUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
            class constructure
        """
        self.blocks = {}
        super().__init__()

    def __get_lfu(self):
        """
            Method that returns the Least Frequently Used item
            if there is more than 1 item
            it returns the Lease Recently (LRU) Used item
        """
        sort = dict(sorted(self.blocks.items(), key=lambda x: x[1]))
        k = list(sort.keys())
        last = None
        more = False
        for item in k:
            if not last:
                last = item
                continue
            if last == item:
                more = True
                break
        if more:
            keys = self.blocks.keys()
            return keys[0]
        else:
            return k[0]

    def put(self, key, item):
        """
            Method that puts key and its item in cache
            with LFU algorithm
        """
        if key and item:
            if len(self.cache_data) < self.MAX_ITEMS:
                if key in self.cache_data:
                    self.blocks[key] += 1
                else:
                    self.blocks[key] = 0
                self.cache_data[key] = item
            else:
                if key in self.cache_data:
                    self.blocks[key] += 1
                    self.cache_data[key] = item
                else:
                    k = self.__get_lfu()
                    self.cache_data[key] = self.cache_data.pop(k)
                    self.cache_data[key] = item
                    del self.blocks[k]
                    self.blocks[key] = 0
                    print(f'DISCARD: {k}')

    def get(self, key):
        """
            Method that returns the value of the given key
            if exists with LFU algorithm
        """
        if key and key in self.cache_data:
            self.blocks[key] += 1
            return self.cache_data[key]
        return None
