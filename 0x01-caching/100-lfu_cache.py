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
        self.order = []

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
                lfu_keys = [
                    k for k, v in self.frequency.items()
                    if v == self.min_frequency
                ]
                if len(lfu_keys) == 1:
                    discarded_key = lfu_keys[0]
                else:
                    lru_key = next((
                        k for k in self.order if k in lfu_keys
                    ), None)
                    discarded_key = lru_key

                if discarded_key is not None:
                    del self.cache_data[discarded_key]
                    del self.frequency[discarded_key]
                    self.order.remove(discarded_key)
                    print("DISCARD: {}".format(discarded_key))

                if len(self.cache_data) > 0:
                    self.min_frequency = min(self.frequency.values())
                else:
                    self.min_frequency = 0

            self.cache_data[key] = item
            self.update_frequency(key)
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.update_frequency(key)
            return self.cache_data[key]
        return None
