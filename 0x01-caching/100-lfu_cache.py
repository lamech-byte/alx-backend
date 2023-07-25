#!/usr/bin/env python3
"""
100-lfu_cache.py
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.frequency = {}
        self.min_frequency = 0

    def update_frequency(self, key):
        """ Update frequency of the key """
        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_keys = [k for k, v in self.frequency.items() \
                            if v == self.min_frequency]
                if len(lfu_keys) == 1:
                    del self.cache_data[lfu_keys[0]]
                    del self.frequency[lfu_keys[0]]
                    print("DISCARD: {}".format(lfu_keys[0]))
                else:
                    lru_key = None
                    for k in self.order:
                        if k in lfu_keys:
                            lru_key = k
                            break
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    self.order.remove(lru_key)
                    print("DISCARD: {}".format(lru_key))
            self.cache_data[key] = item
            self.update_frequency(key)
            self.order.append(key)
            self.min_frequency = 1

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.update_frequency(key)
            return self.cache_data[key]
        return None
